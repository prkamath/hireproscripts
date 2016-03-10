DB_TENANT_ID=1375
#DB_TENANT_ID=636
#DB_TENANT_ID=586 #"pofu"
SPOC_CREATED_BY=6492
OUTBOUND_CALL = 16505 #call_type -> id from catalog_values where value = "OutBoundCall" and tenant_id = 1	
COMPLETED_CALL = 16512 # id from ccatalog_values where value = "Completed" and tenant_id = 1
XCEL_SHEET_NAME="/home/naveena/Desktop/Office/Code/BulkImport/hireproscripts/xcel/New.xlsx"
#XCEL_SHEET_NAME="/home/kamath/source/scripts/hireproscripts/xcel/NewBook.xlsx"

START_ROW_TO_PARSE=23
MAX_ROWS_TO_PARSE=2158
MAX_ROWS_TO_CREATE=2158
#MAX_ROWS_TO_PARSE=25
#MAX_ROWS_TO_CREATE=25
VERBOSE_DEBUG_SETTING=1

if (DB_TENANT_ID == 1375):
    DB_IP= ""
    DB_USER=""
    DB_PASSWORD=""
    DB_DBNAME=""
else:
    DB_IP="10.0.5.88"
    DB_USER="ashish"
    DB_PASSWORD="data"
    DB_DBNAME="appserver_core"

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


def populateMetaData(spocdict,query_cat_dict,query_criticality_dict, status_dict):
    if (DB_TENANT_ID == 636):
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
    if (DB_TENANT_ID == 636):
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
        tempDict = {
            "declined": { # stage id = 142037
                "offer declined" : {
                     "id" : 142038,	
                     "reasons" : {
			     "company retained":524 ,
			     "counter offer":525 ,
			     "date of joining":526 ,
			     "delayed offer":527 ,
			     "designation":528 ,
			     "employment contract":529 ,
			     "higher studies":532 ,
			     "illness":533 ,
			     "location constraints":534 ,
			     "low salary":535 ,
			     "offer revoked":536 ,
			     "onsite opportunity":537 ,
			     "personal reasons":538 ,
			     "shifts":539 ,
			     "technology":540 ,
			     "travel":541 ,
			     "others":542 ,
			     "family constraints":544 ,
			     "family constraint":544 ,
			     "bgv negative":545,
                             "behavioural concerns" : 552  ,
                             "behavioral concerns" : 552
		     }
                },
                "offer declined - willing to negotiate" : {
                     "id" : 142038,	
                     "reasons" : {
			     "company retained":524 ,
			     "counter offer":525 ,
			     "date of joining":526 ,
			     "delayed offer":527 ,
			     "designation":528 ,
			     "employment contract":529 ,
			     "higher studies":532 ,
			     "illness":533 ,
			     "location constraints":534 ,
			     "low salary":535 ,
			     "offer revoked":536 ,
			     "onsite opportunity":537 ,
			     "personal reasons":538 ,
			     "shifts":539 ,
			     "technology":540 ,
			     "travel":541 ,
			     "others":542 ,
			     "family constraints":544 ,
			     "bgv negative":545,
                             "behavioural concerns" : 552, #NAVEENA
		     }
                 }
	    },
            "dropped" : { # stage id = 142035
                "dropped" : {
                    "id" : 142036,
                    "reasons" : {
                        "bgv negative":519 ,
                        "document insufficient":520 ,
                        "behavioural concerns":521 ,
                        "behavioral concerns":521 ,
                        "not reachable":522 ,
                        "offer revoked":551, # NAVEENA
		    }
                },
                "offer declined" : {
                    "id" : 142036,
                    "reasons" : {
                        "bgv negative":519 ,
                        "document insufficient":520 ,
                        "behavioural concerns":521 ,
                        "not reachable":522 ,
                        "offer revoked":551,#NAVEENA
		    }
                },
                "offer declined - willing to negotiate" : {
                    "id" : 142036,
                    "reasons" : {
                        "bgv negative":519 ,
                        "document insufficient":520 ,
                        "behavioural concerns":521 ,
                        "not reachable":522 ,
                        "offer revoked":551,#NAVEENA
		    }
                }
            },
            "joining" : { # stage id = 142039
                "joined"  : {
                    "id" : 142040,
                    "reasons" : {
                    }
                 }
            },
            "yet to join" : { #stage id = 142022
                "bgv yet to complete / initiate": {
                    "id":142023,
                    "reasons": {
                    }
                 },
                "yet to accept": {
                    "id" : 142026,
                    "reasons" : {
                        "low salary":548,
                    }
		},
                "no response": {
                    "id" : 142054,
                    "reasons" : {
                    }
		},
                "offered": {
                    "id" : 142605,
                    "reasons" : {
                    }
                },
                "offer letter not received": {
                    "id" : 142027,
                    "reasons" : {
                    }
                },
                "offer accepted & doj to be confirmed with queries": {
                    "id" : 142028,
                    "reasons" : {
                    }
		},
                "offer accepted & doj to be confirmed": {
                    "id":142029,
                    "reasons" : {
                        "date of joining" : 550 #NAVEENA
                    }
                },
                "offer accepted & doj confirmed with queries": {
                    "id":142030, 
                    "reasons" : {
                    }
		},
                "offer accepted & doj confirmed": {
                    "id":142031, 
                    "reasons" : {
                        "counter offer": 549, #NAVEENA
                    } 
                },
                "joining date elapsed": {
                    "id":142032,
                    "reasons": {
                        "delayed offer" : 546,
                        "low salary" : 547,
                    }
                },
                "invalid contact details": {
                    "id":142033, 
                    "reasons" : {
                    }
                },
                "invalid contact details / out of india": {
                    "id":142033, 
                    "reasons" : {
                    }
                },
                "yet to initiate pofu": {
                    "id":142034, 
                    "reasons" : {
                    }
                },
                "no response": {
                    "id":142054,
                    "reasons" : {
                    }
                }
            }
        }
    for tmpkey in tempDict.keys():
        status_dict[tmpkey]=tempDict[tmpkey]
    print status_dict
    #1646 => Dropped/Offer Declined with Declined Reasons Offer Revoked.. 
    #1815 => Declined/Offer Declined-Willing to Negotiate Low Salary
    #1538 => Dropped/Offer Declined - Document Insufficient
    #344  => Joining and Joined and but decined reason..
