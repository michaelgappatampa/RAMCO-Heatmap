import requests;
import os;

RAMCO_API_KEY = os.getenv("RAMCO_API_KEY");

class RamcoOperations:
    def pullRAMCOdata(entity, filter, attributes):
        data = {
            "Key" : RAMCO_API_KEY,
            "Operation" : "GetEntities",
            "entity" : entity,
            "filter" : filter,
            "attributes" : attributes
        }
        records = requests.post("https://api.ramcoams.com/api/v2/", data=data);
        return records;

    def paginateRecords(data,streamToken):
        if streamToken != None:
            data = {
            "Key" : RAMCO_API_KEY,
            "Operation" : "GetEntities",
            "StreamToken" : streamToken
        }
            records = requests.post("https://api.ramcoams.com/api/v2/", data=data);
        return records;

    def updateRecord(recordId,entity,attributeValue):
        data = {
            "Key" : RAMCO_API_KEY,
            "Operation" : "UpdateEntity",
            "entity" : entity,
            "GUID" : recordId,
            "AttributeValue" : attributeValue
        }
        requests.post("https://api.ramcoams.com/api/v2/", data=data);
        print("RECORD Updated: " + recordId)