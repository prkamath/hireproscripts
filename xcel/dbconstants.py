DB_IP="10.0.5.88"
DB_USER="ashish"
DB_PASSWORD="data"
DB_DBNAME="appserver_core"
DB_TENANT_ID=1375
SPOC_CREATED_BY=6492
XCEL_SHEET_NAME="/home/kamath/source/scripts/hireproscripts/xcel/Book3.xlsx"
MAX_ROWS_TO_PARSE=20

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


def populateMetaData(spocdict,query_cat_dict,query_criticality_dict):
    spocdict['Akanksha']=16049
    spocdict['Soumya']=16050
    spocdict['Riya']=16052
    spocdict['Dhivya']=16053

    query_cat_dict["CTC Revisions"]=1
    query_cat_dict["Joining bonus"]=2
    query_cat_dict["Location change"]=3
    query_cat_dict["Accommodation eligibility"]=4
    query_cat_dict["Role Clarity"]=5
    query_cat_dict["Offer letter not received"]=6
    query_cat_dict["Links not received"]=7
    query_cat_dict["Unable to upload documents"]=8
    query_cat_dict["Mismatch in candidate details"]=9
    query_cat_dict["Insufficient Document"]=10
    query_cat_dict["Awaiting for Joining booklet"]=11
    query_cat_dict["Date of Joining Confirmation"]=12
    query_cat_dict["DOJ Extension"]=13
    query_cat_dict["NA"]=14

    query_criticality_dict['Level 1']=1
    query_criticality_dict['Level 2']=2
    query_criticality_dict['Level 3']=3
    query_criticality_dict['No Query']=4