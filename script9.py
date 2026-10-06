import psutil
import sys

report = "process_report.txt"
name = sys.argv[1]

proc=[]

for p in psutil.process_iter(['name']):
    try:
        if p.info['name'] == name:
            proc.append(p)
    except:
        pass

with open(report, "w") as f:

    f.write("Process Information Report\n\n")

    if len(proc)>0:
        f.write("Process Found! \n\n")
        f.write("Process PIDs are: \n")
        cpu=0
        mem=0
        for p in proc:
            f.write(str(p.pid)+" ")
            try:
                cpu+=p.cpu_percent(interval=0.1)
                mem+=p.memory_info().rss
            except:
                pass
        f.write("\n\n")
        f.write("Total CPU Usage:\n")
        f.write(str(cpu) + "\n\n")

        f.write("Total Memory Usage:\n")
        f.write(str(mem) + "\n\n")

    else:
        f.write("Process not found!\n")


print("Report saved successfully, check", report, "for further details!")