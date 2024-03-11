import requests
import json

URL = 'http://127.0.0.1:8000/topucretae/'

data ={
    'id':1,
    'teacher_name':'shamim Ahmmed ',
    'course_duration':'45',
   
}

json_data = json.dumps(data)
r= requests.put(url=URL, data=json_data)
if r.status_code == 200:
    print(r.json())
    
else:
    print(f"error:{r.status_code}")