# -*- coding: utf-8 -*-
import requests
import json

appid = "5a200ce8e6ec3a6506030e54ac3b970e"
register_data = {"cmd": "chat", "appid": appid, "userid": "812ef0164a8c98d0c9c2b7fc497b5758", "text": "好气啊", "location": ""}
url = "http://idc.emotibot.com/api/ApiKey/openapi.php"
r = requests.post(url, params=register_data)
response = json.dumps(r.json(), ensure_ascii=False)
jsondata = json.loads(response)
print("Return: %s" % jsondata.get("return"))
print("ReturnMessage: %s" % jsondata.get("return_message"))
datas = jsondata.get("data")
for data in datas:
    print("Value: %s" % data.get('value'))
    print("Type: %s" % data.get('type'))
    print("Cmd: %s" % data.get('cmd'))
    print("Data: %s" % data.get('data'))

dataemotions = jsondata.get("emotion")
for dataemotion in dataemotions:
    print("Score: %s" % dataemotion.get("score"))
    print("Data: %s" % dataemotion.get("data"))
    print("Value: %s" % dataemotion.get("value"))
    print("Type: %s" % dataemotion.get("type"))
