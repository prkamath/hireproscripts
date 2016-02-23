DB_IP="10.0.5.88"
DB_USER="ashish"
DB_PASSWORD="data"
DB_DBNAME="appserver_core"
#DB_TENANT_ID=1375
DB_TENANT_ID=586
SPOC_CREATED_BY=6492
XCEL_SHEET_NAME="/home/kamath/source/scripts/hireproscripts/xcel/Book3.xlsx"
MAX_ROWS_TO_PARSE=25

SERVICE_URL="http://%s:8000//py/api/v1/bulkimport"
SERVICE_IP="10.0.5.88"
AUTH_TOKEN='86af4a75-1662-46b9-940e-5e1531eaf928'

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


def populateMetaData(spocdict,query_cat_dict,query_criticality_dict, status_dict):
    spocdict['Akanksha']=16049
    spocdict['Soumya']=16050
    spocdict['Riya']=16052
    spocdict['Dhivya']=16053

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
        "Yet to Initiate POFU":142034,
        "Dropped":142035,
        "Dropped":142036,
        "Declined":142037,
        "Declined":142038,
        "Joining":142039,
        "Joined":142040,
        "Offer Declined":142012#TODO
    }
    for val in tempDict.keys():
        status_dict[val.lower()]=tempDict[val]
    print status_dict
