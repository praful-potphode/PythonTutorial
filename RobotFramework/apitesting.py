import requests
import os

from robot.libraries.BuiltIn import BuiltIn
response=requests.get("http://dummy.restapiexample.com/api/v1/employees")
# params={"id":1}
response=requests.get(url="http://dummy.restapiexample.com/api/v1/employee/1",headers={"User-Agent": "XY"})
print(response.status_code)
print(response.json())

# req_body = {'name': 'kyle pogi1',
#                 'salary': '3232323',
#                 'age': '34'}
#
# response = requests.post(url='http://dummy.restapiexample.com/api/v1/create', data=req_body)
# print(response.status_code)
# print(response.json())

def list_users(apiname,endpoint):
    uri=get_uri(apiname)
    response=requests.get(endpoint+uri)
    os.environ['RESPONSE']=str(response.json())
    BuiltIn().log('Response ' + str(os.environ['RESPONSE']) + ' is displayed')
    os.environ['STATUS CODE'] = str(response.status_code)
def get_uri(apiname):
    if apiname == 'LISTUSERS':
        uri='/api/users?page=2'
    elif apiname == 'CREATEUSER':
        uri='/api/users'
    elif apiname == 'DELETEUSER':
        uri='/api/users/'
    else:
        uri = '/api/users/2'

    return uri
def verify_status_code(statuscode):
    if statuscode == os.environ['STATUS CODE']:
        BuiltIn().log('Status code '+str(statuscode)+' is displayed')
    else:
        BuiltIn().log(message='Status code '+str(statuscode)+' is displayed',level='ERROR')
def update_user(apiname,endpoint,data):
    uri=get_uri(apiname)
    response=requests.put(url=endpoint+uri,data=data)
    os.environ['RESPONSE']=str(response.json())
    BuiltIn().log('Response ' + str(os.environ['RESPONSE']) + ' is displayed')
    os.environ['STATUS CODE'] = str(response.status_code)
def create_user(apiname,endpoint,data):
    uri=get_uri(apiname)
    response=requests.post(url=endpoint+uri,data=data)
    os.environ['RESPONSE']=str(response.json())
    BuiltIn().log('Response ' + str(os.environ['RESPONSE']) + ' is displayed')
    os.environ['STATUS CODE'] = str(response.status_code)
def delete_user(apiname,endpoint,userid):
    uri=get_uri(apiname)
    print(endpoint+uri+userid)
    response=requests.delete(url=endpoint+uri+userid)
    # os.environ['RESPONSE']=str(response.json())
    BuiltIn().log('Response ' + str(os.environ['RESPONSE']) + ' is displayed')
    os.environ['STATUS CODE'] = str(response.status_code)
