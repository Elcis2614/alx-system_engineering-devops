#!/usr/bin/python3
""" Given the API, for a given employee ID, returns information about his/her TODO list progress. """
import json
import sys
import urllib.request as lib

if __name__ == "__main__":
    dataSrc = lib.urlopen('https://jsonplaceholder.typicode.com/todos')
    data = json.loads(dataSrc.read())

    userSrc = lib.urlopen('https://jsonplaceholder.typicode.com/users')
    users = json.loads(userSrc.read())
    cust_id = int(sys.argv[1])

    custName = "DUMB"
    for a_dict in users:
        if (cust_id == int(a_dict["id"])):
            custName = a_dict["name"]
            break
    customer = {"name": custName, "tasks": [], "maxTask" : 0, "doneTask" : 0}

    for a_dict in data :
        if (a_dict["userId"] == cust_id):
            customer["maxTask"] += 1;
            if a_dict["completed"] :
                customer["tasks"].append(a_dict["title"])
                customer["doneTask"] += 1

    print("Employee {} is done with tasks({}/{}):".format(custName, customer["doneTask"], customer["maxTask"]))
    for task in customer["tasks"]:
        print("\t {}".format(task))
