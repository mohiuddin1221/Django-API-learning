import requests
import json

URL = 'http://127.0.0.1:8000/topucretae/'

data= {
    'id': 3
}
json_data = json.dumps(data)
r = requests.delete(url=URL,data=json_data)

if r.status_code==200:
    print(r.json())
    
else:
    print(f"error : {r.status_code}")