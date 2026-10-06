import subprocess
import sys

report = "login_report.txt"

user = sys.argv[1]

with open(report, "w") as f:

    f.write("User login report\n\n")

    f.write("Currently logged-in users:\n")
    who = subprocess.getoutput("who")
    f.write(who + "\n\n")

    f.write("Number of logged-in users:\n")
    users = who.splitlines()
    f.write(str(len(users)) + "\n\n")

    if user in who:
        f.write(user + " is currently logged in.\n")
    else:
        f.write(user + " is not currently logged in.\n")

    f.write("\n")

    f.write("Last 10 users logins:\n")
    last = subprocess.getoutput("last")
    last_lines = last.splitlines()
    f.write("\n".join(last_lines[:10]) + "\n\n")

    f.write("Number of unique users who logged in:\n")

    unique_users = set()

    for line in last_lines:
        parts = line.split()

        if len(parts) > 0:
            unique_users.add(parts[0])

    f.write(str(len(unique_users)) + "\n\n")

    f.write("The most recent logins:\n")
    f.write("\n".join(last_lines[:3]) + "\n")

    # Added a new line here

print("Report saved successfully, check", report, "for further details!")