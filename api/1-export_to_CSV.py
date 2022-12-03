#!/usr/bin/python3
"""Module to export data in a csv file"""


import requests
import json
import sys
import csv

#to get the user id

id = sys.argv[1]

#to fetch all the data we want from /todos and /users

users_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
users_names = requests.get('https://jsonplaceholder.typicode.com/users')

#to use the data we just fetched

todos_data = users_todos.text
users_data = users_names.text

#to transform this data into python object

parse_todos = json.loads(todos_data)
parse_users = json.loads(users_data)

for key in parse_users:
    if key['id'] == int(id):
        username = key['name']

all_datas = []
    
for item in parse_todos:
    if item['userId'] == int(id):
        listing = [id, username, item['completed'], item['title']]
        all_datas.append(listing)
filename = id + ".csv"
    
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, doublequote= True, quotechar='"')
    
    for i in all_datas:
        writer.writerow(i)
        
print('done')
