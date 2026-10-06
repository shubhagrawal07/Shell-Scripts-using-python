import os

path = "students.csv"

for root, dir, files in os.walk(os.getcwd()):
    for file in files:
        if file==path:
            cse=0
            ee=0
            lines=0
            path = os.path.join(root,path)
            with open(path) as csv:
                for line in csv:
                    if "CSE" in line:
                        cse+=1
                    if "EE" in line:
                        ee+=1
                    lines+=1
            print(lines)
            print(cse)
            print(ee)

        