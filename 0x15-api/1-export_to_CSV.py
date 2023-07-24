#!/usr/bin/python3
""" Given the API, for a given employee ID, returns information
about his/her TODO list progress. """
import csv
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
            custName = a_dict["username"]
            break
    with open('{}.csv'.format(cust_id), 'w', newline='') as mFile:
        writter = csv.writer(mFile, delimiter=',', quoting=csv.QUOTE_ALL)
        for a_dict in data:
            if (a_dict["userId"] == cust_id):
                writter.writerow(
                    [cust_id, custName, a_dict["completed"], a_dict["title"]])
