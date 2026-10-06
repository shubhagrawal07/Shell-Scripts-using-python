import psutil
import sys
import subprocess

report = "login_report.txt"

user = sys.argv[1]

users = psutil.users()

unique_users = sorted(set(user.name for user in users))

with open(report, "w") as f:

    f.write("User login report\n\n")

    f.write("Currently logged-in users:\n")
    f.write(" ".join(unique_users) + "\n\n")

    f.write("Current logged users time: ")
    for user in users:
        f.write(f"{user.name} {user.started}" + "\n\n")

    f.write("Number of logged-in users:\n")
    f.write(str(len(unique_users)) + "\n\n")


    if user in unique_users:
        f.write(f"{user} +  is currently logged in.\n")
    else:
        f.write(f"{user} +  is not currently logged in.\n")

    f.write("\n")

    f.write("Last 10 users logins:\n")
    last = subprocess.getoutput("last")
    last_lines = last.splitlines()
    f.write("\n".join(last_lines[:10]) + "\n\n")

    f.write("Number of unique users who logged in: \n")
    f.write(str(len(unique_users)))

    



print("Report saved successfully, check", report, "for further details!")