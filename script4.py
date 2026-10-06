import os

project = "testdir"

filemp = {}

if os.path.isdir(project):
    for root, dirs, files in os.walk(project):
        for file in files:
            if file in filemp:
                filemp[file]+=1
            else:
                filemp[file]=1

for key,value in filemp.items():
    if value>1:
        print(key)