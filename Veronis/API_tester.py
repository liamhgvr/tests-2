# API Tester

import requests
import pytest

headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'}
body = {"username": "test", "password": "1234"}
url = 'http://localhost:8000'

def setUp():
    # Get Auth and build Headers
    acc_token = requests.post("http://localhost:8000/api/auth", headers=headers, json=body).json()['access_token']
    headers['Authorization'] = 'Bearer {}'.format(acc_token)

# Body
body = { "data": [ { "key": "key1", "val": "val1", "valType": "str" } ] }

#res = requests.get(url + '/api/poly', headers=headers)
#res2 = requests.post(url + '/api/poly', headers=headers, json=body)
res3 = requests.get(url + '/api/poly' + '/1', headers=headers)
#res4 = requests.delete(url + '/api/poly', headers=headers)
print(res3.text)
#print(res2.text)
#print(res3.text)

@pytest.
def sanity_test():
    body = { "data": [ { "key": "key1", "val": "val1", "valType": "str" } ] }
