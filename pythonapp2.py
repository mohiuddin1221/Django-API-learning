import requests
import json
URL = 'http://127.0.0.1:8000/topucretae/'

data ={
    'teacher_name':'Keya',
    'course_name': 'Acc',
    'course_duration':'25',
    'seat': '35'
}

json_data = json.dumps(data)
r = requests.post(url = URL, data=json_data)
if r.status_code == 200:
    # Print the response JSON data
    print(r.json())
else:
    # Print an error message if the request was not successful
    print(f"Error: {r.status_code}")
    
    
    
