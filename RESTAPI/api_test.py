# importing the requests library
import requests

response=requests.get('https://reqres.in/api/users?page=2')
if response.status_code==200:
    # extracting data in json format
    data = response.json()

    email=data['data'][0]['email']
    avatar=data['data'][0]['avatar']
    first_name=data['data'][0]['first_name']
    last_name=data['data'][0]['last_name']

    # printing the output
    print("first_name:%s\nlast_name:%s\nemail:%s"
        %(first_name, last_name,email))
else:
    print('response was not successful,response code recieved is '+response.status_code)

input='{"name": "morpheus", "job": "zion resident"}'
response=requests.put(url='https://reqres.in/api/users/2',data=input)
print(response.json())
