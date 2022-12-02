#!/usr/bin/python3

import requests
import json
import sys

id = sys.argv[1]
print(id)

users_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
users_names = requests.get('https://jsonplaceholder.typicode.com/users')

#print(api_response.status_code)

todos_data = users_todos.text
users_data = users_names.text

parse_todos = json.loads(todos_data)
parse_users = json.loads(users_data)


tasks = []
username = None

for key in parse_users:
    if key['id'] == int(id):
        username = key['name']

for item in parse_todos:
    if item['userId'] == int(id):
        tasks.append(item)
        
tasks_done = 0
completed_tasks =[]
tasks_left = 0

for i in tasks:
    if i['completed'] == True:
        tasks_done = tasks_done + 1
        completed_tasks.append(i['title'])
        
for i in tasks:
    if i['completed'] == False:
        tasks_left = tasks_left + 1
        
all_tasks = tasks_left + tasks_done


print ("Employee {} is done with tasks ({}/{}):".format(username, tasks_done, all_tasks))
for i in completed_tasks:
    print("\t {}".format(i))