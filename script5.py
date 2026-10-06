import os
import sys

path = os.path.expanduser("~")

def solver(directory):
    for root,dir,files in os.walk(path):
        for dr in dir:
            if dr==directory:
                print(directory, " Exists!!!")
                relpath = os.path.join(root,dr)
                return relpath

    return ""

for arg in sys.argv[1:]:
    relpath = solver(arg)
    if relpath!="":
        count=0
        sz=0
        for root,dir,files in os.walk(relpath):
            for file in files:
                count+=1
                sz+=os.path.getsize(os.path.join(root,file))
            for dr in dir:
                sz+=os.path.getsize(os.path.join(root,dr))

        print("No of files: ", count)
        print("Directory Size: ", sz)

        if sz<100*1024*1024:
            print("Small")
        elif sz<1024*1024*1024:
            print("Medium")
        else:
            print("Large")
    else:
        print(arg," Does not exists!")