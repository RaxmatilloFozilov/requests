import httpx
from pprint import pprint
import os
import json
url='https://jsonplaceholder.typicode.com/users'
response=httpx.get(url=url)
data =response.json()
# os.mkdir('user')
# pprint(response.json())
print(data)
os.chdir('user')
for user in data:
    # print(user['id'])
    with open(f"{user['id']}.txt",'w') as f:
        f.write(f"Name: {user['name']}")
        f.write(f"Phone: {user['phone']}")
        f.write(f"User Name{user['username']}")
        f.write(f"Web site: {user['website']}")