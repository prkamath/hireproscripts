from dbconstants import *
import MySQLdb
from openpyxl import load_workbook
from datetime import datetime

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
    tempstring="insert into candidate_spocs (candidate_id,user_id,guid,is_deleted,created_on,created_by) values (%d,%d,%s,0,now(),%d)"\
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

def insertCandStaffingQueries

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

    for row in ws.iter_rows(row_offset=1):
        singleRow={}
        ret=parseRowIntoDict(row,singleRow)
        singleRow['candidatestaffingprofileid']= getCandidateStaffingProfileId(singleRow['EmailId'])
        if (0 == ret):
            allRows.append(singleRow)


    for singleRow in allRows:
        updateCandidateStaffingProfile(singleRow['candidatestaffingprofileid'],singleRow['ExpectedDOJ'])
        createCandSpocs(singleRow['CandidateId'],singleRow['spocname'],spocdict)
        if (count<=4):
            print row['CallStatus']
            count=count+1

    print "Total rows=" + str(len(allRows))

'''
    checkForUsers(["prkamath@gmail.com","sheela@we.com"])
    checkForCandidates(["prkamath@gmail.com","sheela@we.com"])
'''
