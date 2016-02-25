DB_IP="10.0.5.88"
DB_USER="ashish"
#DB_IP="127.0.0.1"
#DB_USER="appserver"
DB_PASSWORD="data"
DB_DBNAME="appserver_core"
#DB_TENANT_ID=1375
DB_TENANT_ID=586
SPOC_CREATED_BY=6492
OUTBOUND_CALL = 16505 #call_type -> id from catalog_values where value = "OutBoundCall" and tenant_id = 1	
COMPLETED_CALL = 16512 # id from ccatalog_values where value = "Completed" and tenant_id = 1
XCEL_SHEET_NAME="/home/kamath/source/scripts/hireproscripts/xcel/NewBook.xlsx"
START_ROW_TO_PARSE=120
MAX_ROWS_TO_PARSE=10
MAX_ROWS_TO_CREATE=25
VERBOSE_DEBUG_SETTING=1

SERVICE_URL="http://%s:8000//py/api/v1/bulkimport"
SERVICE_IP="10.0.5.88"
AUTH_TOKEN='0039b8ba-1632-4645-99be-170645eb995e'

template= """{
  "type": "offerImport",
  "candidateList": [
    {
      "OriginalSourceID": "9900112",
      "Name": "ussab12121",
      "Mobile1": "28872228122",
      "Email1": "prkamahesh@gmail.com",
      "Level": "L1",
      "OfferedBU\/Unit\/Department": "BFSI",
      "ActualWorkLocation": "Bangalore",
      "PrimaryRecruiterName": "Ramesh",
      "LevelId": "15141",
      "OwningDepartmentId": "2353",
      "LocationOfferedId": "1809",
      "OfferedBUId": "2353",
      "LocationPreferenceId": "1808",
      "SkillCategoryId": "15148",
      "validateObj": [

      ],
      "errorObj": null,
      "isValid": true,
      "status": 0,
      "isSaved": false,
      "OwningDepartmentText": "Default"
    }
  ]
}"""


def populateMetaData(spocdict,query_cat_dict,query_criticality_dict, status_dict,reasons_dict):
    if (DB_TENANT_ID == 586):
        spocdict['Akanksha']=9745
        spocdict['Soumya']=9745
        spocdict['Riya']=9745
        spocdict['Dhivya']=9745
        spocdict['Bhanu']=9745
        spocdict['Dilna']=9745
    else:
        spocdict['Akanksha']=16366
        spocdict['Soumya']=16365
        spocdict['Riya']=16367
        spocdict['Dhivya']=16368
        spocdict['Bhanu']=16364
        spocdict['Dilna']=16369

    query_cat_dict["CTC Revisions"]=36161
    query_cat_dict["Joining bonus"]=36157
    query_cat_dict["Location change"]=36168
    query_cat_dict["Accommodation eligibility"]=36167
    query_cat_dict["Role Clarity"]=36169
    query_cat_dict["Offer letter not received"]=36159
    query_cat_dict["Links not received"]=36164
    query_cat_dict["Unable to upload documents"]=36166
    query_cat_dict["Mismatch in candidate details"]=36162
    query_cat_dict["Insufficient Document"]=36165
    query_cat_dict["Awaiting for Joining booklet"]=36160
    query_cat_dict["Date of Joining Confirmation"]=36163
    query_cat_dict["DOJ Extension"]=36158
    query_cat_dict["NA"]=None

    query_criticality_dict['Level 1']=36170
    query_criticality_dict['Level 2']=36171
    query_criticality_dict['Level 3']=36172
    query_criticality_dict['No Query']=1
    if (DB_TENANT_ID == 586):
        tempDict={
            "BGV Yet to Complete / Initiate":54764,
            "Yet to Intiate POFU":54764,
            "Yet to Intiate POFU":54765,
            "Yet to Accept":54766,
            "Offer Letter Not Received":54767,
            "Offer Accepted & DOJ To Be Confirmed with Queries":54768,
            "Offer Accepted & DOJ To Be Confirmed":54769,
            "Offer Accepted & DOJ Confirmed with Queries":54770,
            "Offer Accepted & DOJ Confirmed":54771,
            "Joining Date Elapsed":54772,
            "Invalid Contact Details":54764,
            "Invalid Contact Details / Out of India":54764,
            "Yet to Initiate POFU":54764,
            "Dropped":54764,
            "Dropped":54764,
            "Declined":54764,
            "Declined":54764,
            "Joining":54764,
            "Joined":54764,
            "Offer Declined":54764,#TODO
            "offer declined - willing to negotiate":54764,#TODO
            "No Response":54764#TODO
        }
    else:
        tempDict={
            "BGV Yet to Complete / Initiate":142023,
            "Yet to Intiate POFU":142024,
            "Yet to Intiate POFU":142025,
            "Yet to Accept":142026,
            "Offer Letter Not Received":142027,
            "Offer Accepted & DOJ To Be Confirmed with Queries":142028,
            "Offer Accepted & DOJ To Be Confirmed":142029,
            "Offer Accepted & DOJ Confirmed with Queries":142030,
            "Offer Accepted & DOJ Confirmed":142031,
            "Joining Date Elapsed":142032,
            "Invalid Contact Details":142033,
            "Invalid Contact Details / Out of India":142033,
            "Yet to Initiate POFU":142034,
            "Dropped":142035,
            "Dropped":142036,
            "Declined":142037,
            "Declined":142038,
            "Joining":142039,
            "Joined":142040,
            "Offer Declined":142038,#TODO
            "offer declined - willing to negotiate":142038,#TODO
            "No Response":142013,#TODO
            "Offer Declined but like to negotiate":142604,
            "Offered":142605
        }
    for val in tempDict.keys():
        status_dict[val.lower()]=tempDict[val]
    print status_dict

    tmpReasons = {
        "BGV Negative":"519" ,
        "Document Insufficient":"520" ,
        "Behavioural Concerns":"521" ,
        "Not Reachable":"522" ,
        "Company Retained":"524" ,
        "Counter Offer":"525" ,
        "Date of Joining":"526" ,
        "Delayed Offer":"527" ,
        "Designation":"528" ,
        "Employment Contract":"529" ,
        "Higher Studies":"532" ,
        "Illness":"533" ,
        "Location Constraints":"534" ,
        "Low Salary":"535" ,
        "Offer Revoked":"536" ,
        "Onsite Opportunity":"537" ,
        "Personal Reasons":"538" ,
        "Shifts":"539" ,
        "Technology":"540" ,
        "Travel":"541" ,
        "Others":"542" ,
        "Family Constraints":"544" ,
        "BGV Negative":"545" 
    }
    for val in tempReasons.keys():
        reasons_dict[val.lower()]=tempReasons[val]
    print reasons_dict 
