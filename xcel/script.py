from dbconstants import *
import MySQLdb
from openpyxl import load_workbook
from datetime import datetime
import uuid

def checkForCandidates(candidatelist):
    db = MySQLdb.connect(host=DB_IP,    # your host, usually localhost
            user=DB_USER,         # your username
            passwd=DB_PASSWORD,  # your password
            db=DB_DBNAME)        # name of the data base
    cur = db.cursor()
    totalexistingcandidates=0
    print "\n===========================================\n"
    print "The emails we will test for are",candidatelist
    print "\n===========================================\n"
    for emailid in candidatelist:
        fetched=0
        tempString="select id,email1 from candidates where email1='%s'"%emailid
        cur.execute(tempString)
        for row in cur.fetchall():
            print row
            fetched=1
        if (fetched==1):
            totalexistingcandidates=totalexistingcandidates+1
        else:
            print "Unable to fetch record for " + emailid
    print "Total fetched candidates are " + str(totalexistingcandidates) 
    db.close()

def checkForUsers(userlist):
    db = MySQLdb.connect(host=DB_IP,    # your host, usually localhost
            user=DB_USER,         # your username
            passwd=DB_PASSWORD,  # your password
            db=DB_DBNAME)        # name of the data base
    cur = db.cursor()
    totalexistingusers=0
    print "\n===========================================\n"
    print "The emails we will test for are",userlist
    print "\n===========================================\n"
    for emailid in userlist:
        fetched=0
        tempString="select id,email1 from users where email1='%s'"%emailid
        cur.execute(tempString)
        for row in cur.fetchall():
            print row
            fetched=1
        if (fetched==1):
            totalexistingusers=totalexistingusers+1
        else:
            print "Unable to fetch record for " + emailid
    print "Total fetched users are " + str(totalexistingusers) 
    db.close()

def makeSenseOfDate(inDate):
    if (inDate.lower().find("jan")>-1 or inDate.lower().find("feb")>-1):
        outDate=inDate + " 2016"
        return outDate
    outDate=inDate+" 2015"
    return outDate

def parseRowIntoDict(row,singleRow):
    if (row[0].value==None):
        return -1
    singleRow['CandidateId']=row[0].value
    singleRow['EmailId']=row[3].value
    singleRow['ExpectedDOJ']=row[12].value
    singleRow['LastDateCalled']=row[13].value
    singleRow['Action']=row[14].value
    singleRow['Inconsistencies']=[]
    singleRow['spocname']=row[25].value
    tempQueryDetails={}
    singleRow['QueryDetails']=tempQueryDetails
    try:
        tempQueryDetails['QueryLevelRaised']=row[15].value
        tempQueryDetails['QueryType']=row[16].value
        tempQueryDetails['QueryRaisedDate']=row[17].value
        tempQueryDetails['QueryResolvedDate']=row[18].value

        gap=tempQueryDetails['QueryResolvedDate']-tempQueryDetails['QueryRaisedDate']
        tempQueryDetails['NoOfDaysForQueryResolution']=gap.days
    except:
        singleRow['Inconsistencies'].append("DateTimeError")

    singleRow['JoiningStatus']=row[21].value
    callStatusDetails=[]
    singleRow['CallStatus']=callStatusDetails
    allDetails=row[22].value.splitlines()
    for detail in allDetails:
        detail=detail.encode("utf-8")
        detail=detail.replace('\xe2\x80\x93','-')
        detail=detail.replace(':','-')
        commentDate=detail.split("-")[0]
        print commentDate
        newcommentDate=makeSenseOfDate(commentDate)
        print newcommentDate
        newcommentDate=newcommentDate.replace("th","")
        try:
            finalDate=datetime.strptime(newcommentDate,"%d %b %Y")
        except:
            continue

        singleConvrsn={}
        singleConvrsn['date']=finalDate
        singleConvrsn['comment']=detail.split("-")[1]
        callStatusDetails.append(singleConvrsn)

    return 0

def getCandidateStaffingProfileId(email):
    db = MySQLdb.connect(host=DB_IP,    # your host, usually localhost
            user=DB_USER,         # your username
            passwd=DB_PASSWORD,  # your password
            db=DB_DBNAME)        # name of the data base
    cur = db.cursor()

    tempString="select candidatestaffingprofile_id from candidates where email1='%s'"%email
    cur.execute(tempString)
    row=cur.fetchone()
    if (row == None):
        return -1
    candId=row[0]
    db.close()
    return candId

def getCandidateId(email):
    db = MySQLdb.connect(host=DB_IP,    # your host, usually localhost
            user=DB_USER,         # your username
            passwd=DB_PASSWORD,  # your password
            db=DB_DBNAME)        # name of the data base
    cur = db.cursor()

    tempString="select id from candidates where email1='%s'"%email
    cur.execute(tempString)
    row=cur.fetchone()
    if (row == None):
        return -1
    candId=row[0]
    db.close()
    return candId

def createCandSpocs(candidateid,spocName,spocDict):
    db = MySQLdb.connect(host=DB_IP,    # your host, usually localhost
            user=DB_USER,         # your username
            passwd=DB_PASSWORD,  # your password
            db=DB_DBNAME)        # name of the data base
    cur = db.cursor()
    guidval=uuid.uuid4()
    tempstring="insert into candidate_spocs (version,candidate_id,user_id,guid,is_deleted,created_on,created_by) values (0,%d,%d,'%s',0,now(),%d)"\
               %(candidateid,spocDict[spocName],guidval,SPOC_CREATED_BY)
    print tempstring
    cur.execute(tempstring)
    db.commit()
    db.close()


def updateCandidateStaffingProfile(staffingProfileId,expectedDateOfJoining):
    db = MySQLdb.connect(host=DB_IP,    # your host, usually localhost
            user=DB_USER,         # your username
            passwd=DB_PASSWORD,  # your password
            db=DB_DBNAME)        # name of the data base
    cur = db.cursor()
    dateOfJ=expectedDateOfJoining.strftime('%Y-%m-%d')
    print dateOfJ
    tempString="update candidate_staffing_profiles set expected_joining_date='%s' where id=%d"%(dateOfJ,staffingProfileId)
    print tempString
    cur.execute(tempString)
    db.commit()
    db.close()


def insertCandStaffingQueries(csp_id,q_cat,q_criticality,spoc,is_pending,created_on,resolved_on):
    """
    +------------------------+----------+------+-----+---------+----------------+
    | Field                  | Type     | Null | Key | Default | Extra          |
    +------------------------+----------+------+-----+---------+----------------+
    | id                     | int(11)  | NO   | PRI | NULL    | auto_increment |
    | tenant_id              | int(11)  | YES  | MUL | NULL    |                |
    | created_by             | int(11)  | NO   |     | NULL    |                |
    | created_on             | datetime | NO   |     | NULL    |                |
    | modified_by            | int(11)  | YES  |     | NULL    |                |
    | modified_on            | datetime | YES  |     | NULL    |                |
    | is_pending             | int(11)  | YES  |     | NULL    |                |
    | candstaffingprofile_id | int(11)  | YES  | MUL | NULL    |                |
    | querycategory_id       | int(11)  | YES  |     | NULL    |                |
    | querycriticality_id    | int(11)  | NO   |     | NULL    |                |
    | query_details          | text     | YES  |     | NULL    |                |
    +------------------------+----------+------+-----+---------+----------------+
    """
    db = MySQLdb.connect(host=DB_IP,    # your host, usually localhost
            user=DB_USER,         # your username
            passwd=DB_PASSWORD,  # your password
            db=DB_DBNAME)        # name of the data base
    cur = db.cursor()
    query = """ insert into cand_staffing_querys (tenant_id,created_by,created_on,modified_by,modified_on,
                is_pending,candstaffingprofile_id, 
                querycategory_id, querycriticality_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    q_paramlist = []
    q_paramlist.append(DB_TENANT_ID)
    q_paramlist.append(spoc)
    q_paramlist.append(created_on)
    q_paramlist.append(resolved_on)
    q_paramlist.append(is_pending)
    q_paramlist.append(csp_id)
    q_paramlist.append(q_cat)
    q_paramlist.append(q_criticality)
    cur.execute(query,q_paramlist)
    db.commit()
    db.close()

def createCandidates(allRows):
    for row in allRows:
        print x



if __name__=="__main__":
    #candId=getCandidateStaffingProfileId("prkamath@gmail.com")
    #updateCandidateStaffingProfile(candId,datetime(2016, 1, 28, 0, 0))
    #print candId
    wb2=load_workbook(XCEL_SHEET_NAME)
    sheetnames=wb2.get_sheet_names()
    ws=wb2.active
    count=0
    allRows=[]
    spocdict={}
    spocdict['Akanksha']=16049
    spocdict['Soumya']=16050
    spocdict['Riya']=16052
    spocdict['Dhivya']=16053
    query_cat_dict={}
    query_criticality_dict={}

    for row in ws.iter_rows(row_offset=1):
        singleRow={}
        ret=parseRowIntoDict(row,singleRow)
        if (0==ret) and ('EmailId' in singleRow):
            singleRow['candidatestaffingprofileid']= getCandidateStaffingProfileId(singleRow['EmailId'])
            singleRow['CandidateIdPrimaryKey']=getCandidateId(singleRow['EmailId'])
            allRows.append(singleRow)
        else:
            print singleRow

    #Log the stuff
    count=0
    countMax=4
    for singleRow in allRows:
        if (count<=countMax):
            print singleRow
            count=count+1


    #Now update the DOJ for all entries
    for singleRow in allRows:
        if (singleRow['CandidateIdPrimaryKey'] == -1):
            continue
        updateCandidateStaffingProfile(singleRow['candidatestaffingprofileid'],singleRow['ExpectedDOJ'])
        createCandSpocs(singleRow['CandidateIdPrimaryKey'],singleRow['spocname'],spocdict)
        is_pending = 0
        if 'QueryType' in singleRow:
            insertCandStaffingQueries(singleRow['candidatestaffingprofileid'],
                        query_cat_dict[singleRow['QueryType']],
                        query_criticality_dict[singleRow['QueryLevelRaised']],
                        spocdict[singleRow['spocname']],
                        is_pending,
                        singleRow['QueryRaisedDate'],
                        singleRow['QueryResolvedDate'])

    print "Total rows=" + str(len(allRows))

'''
    checkForUsers(["prkamath@gmail.com","sheela@we.com"])
    checkForCandidates(["prkamath@gmail.com","sheela@we.com"])
'''
