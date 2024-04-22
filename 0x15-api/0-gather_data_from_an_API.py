#!/usr/bin/python3
""" using this REST API, for a given employee ID"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = argv[1]

    user = requests.get(url + f"users/{id}").json()
    params={"userId": id}
    todos = requests.get(url + f"todos").json()
    tasks = [i["title"] for i in todos if i["completed"]]
    print(f"Employee {user.get('name')} is done with ", end="")
    print(f"tasks({len(tasks)}/{len(todos)}):")
    [print(f"\t {i}") for i in tasks]
