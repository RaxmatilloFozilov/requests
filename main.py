import httpx
from pprint import pprint
import os
import json
url='https://jsonplaceholder.typicode.com/todos'
response= httpx.get(url=url)
data = response.json()
# pprint(response.json())
# os.mkdir("todos")

print(data)
os.chdir("todos")
for todo in data:
    # print(todo["id"])
    # print(todo["title"])
    # print(todo["userId"])

    with open(f"{todo['id']}.txt","w") as f:
        f.write(f"Title: {todo['title']}\n")
        f.write(f" User Id{todo['userId']}\n")
