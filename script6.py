import os
import getpass
import socket
import shutil
from datetime import datetime

report = "system_report.txt"

with open(report, "w") as f:

    f.write("<=====System Information Report====>\n\n")

    f.write("Current date and time:\n")
    f.write(str(datetime.now()) + "\n\n")

    f.write("Current user:\n")
    f.write(getpass.getuser() + "\n\n")

    f.write("Hostname:\n")
    f.write(socket.gethostname() + "\n\n")

    f.write("Current working directory:\n")
    f.write(os.getcwd() + "\n\n")

    f.write("Available Disk Space:\n")

    total, used, free = shutil.disk_usage("/")

    f.write("Total: " + str(round(total / (1024 ** 3), 2)) + " GB\n")
    f.write("Used: " + str(round(used / (1024 ** 3), 2)) + " GB\n")
    f.write("Free: " + str(round(free / (1024 ** 3), 2)) + " GB\n\n")

print("Report saved successfully, check", report, "for further details!")