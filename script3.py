import os

path = os.path.expanduser("~")

def dirsize(path):
    total=0;
    for root,dir,files in os.walk(path):
        for file in files:
            relpath = os.path.join(root,file)
            if not os.path.islink(relpath):
                total+=os.path.getsize(relpath)
        for dr in dir:
            relpath = os.path.join(root,dr)
            total+=os.path.getsize(relpath)

    return total

listing = os.listdir(path)

dirs=[]
for list in listing:
    relpath = os.path.join(path,list)
    if os.path.isdir(relpath):
        sz = dirsize(relpath)
        dirs.append((sz,list))

dirs.sort(reverse=True)

for size,item in dirs[:10]:
    size_mb = size/(1024*1024)
    print(f"{size_mb:.2f}MB",item)

