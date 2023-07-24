#!/usr/bin/python3
""" Given the API, for a given employee ID, returns information
about his/her TODO list progress. """

import json
import urllib.request as lib

if __name__ == "__main__":
    dataSrc = lib.urlopen('https://jsonplaceholder.typicode.com/todos')
    data = json.loads(dataSrc.read())

    userSrc = lib.urlopen('https://jsonplaceholder.typicode.com/users')
    users = json.loads(userSrc.read())

    userDict = {}
    for a_dict in users:
        if (a_dict["id"] not in userDict.keys()):
            userDict[a_dict["id"]] = a_dict["username"]

    allDict = {}
    for a_dict in data:
        userId = a_dict["userId"]
        if (userId in allDict.keys()):
            allDict[userId].append({
                "username": userDict[userId],
                "task": a_dict["title"],
                "completed": a_dict["completed"]})
        else:
            allDict[userId] = [{
                "username": userDict[userId],
                "task": a_dict["title"],
                "completed": a_dict["completed"]}]

    with open('todo_all_employees.json', 'w') as mFile:
        json.dump(allDict, mFile)
