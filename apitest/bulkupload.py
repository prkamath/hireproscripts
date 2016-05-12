import json
import copy 
import random
import requests
import sys
#Iaddednew
serviceUrl="http://%s:8000//py/api/v1/bulkimport"
ipOfMachine="10.0.5.88"
iternCount=50
authToken='27e43fe6-3916-41bb-a972-e920675fe036'

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

def attachHeaders(headers,authToken):
    headers['Content-Type']="""application/json; charset=utf-8"""
    headers['X-AUTH-TOKEN']=authToken

    
if __name__=="__main__":
    allDicts=[]
    dict1=json.loads(template)
    candidateList=dict1["candidateList"]
    iternCount=int(sys.argv[1])
    for i in range(0,iternCount):
        tempDict=copy.deepcopy(candidateList[0])
        tempDict["OriginalSourceID"]=str(random.randint(1,99999999999))
        tempDict["Name"]="Kamesh%d"%(random.randint(1,88888888))
        tempDict["Mobile1"]=str(random.randint(1,99999999999))
        tempDict["Email1"]="""pr%d@gml.com"""%random.randint(1,88888888)
        allDicts.append(tempDict)

    dict1["candidateList"]=allDicts
    jsonStr=json.dumps(dict1)
    print jsonStr
    serviceUrl=serviceUrl%(ipOfMachine)
    headers={}
    attachHeaders(headers,authToken)
    ret=requests.post(url=serviceUrl,data=jsonStr,headers=headers)
    print ret.text
