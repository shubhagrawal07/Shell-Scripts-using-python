import os
import sys

directory = sys.argv[1]

if os.path.isdir(directory):
    print("exists")
    listing=[]
    size=0
    for root, dir, files in os.walk(directory):
        for file in files:
            path = os.path.join(root,file)
            listing.append(path)
            size+=os.path.getsize(path)
        for dr in dir:
            path = os.path.join(root,dr)
            size+=os.path.getsize(path)

    print("directory size is: ", size)
    sortedfiles = sorted(listing, key=os.path.getmtime, reverse=True)   
    print("Total files are: ", len(listing))
    print("File listing: ")
    for file in sortedfiles:
        print(os.path.basename(file))
else:
    print("not found")