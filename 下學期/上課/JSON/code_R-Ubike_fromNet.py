import requests
import json
import pandas as pd

data = {'lang':'tw','type':'2'}
r = requests.get("https://apis.youbike.com.tw/api/front/station/all",params=data)
if r.status_code == 200:
    Q1 = r.content.decode('utf-8')
    # str => json
    tmp = json.loads(Q1)
    f = open("data_Ubike.json",'wb')
    # json => str
    Q2 = json.dumps(tmp,indent=4, ensure_ascii=False).encode('utf-8')
    f.write(Q2)

    f.close()
