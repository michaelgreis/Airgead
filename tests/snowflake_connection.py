import subprocess

account = ""
username = ""
password = ""

cmd = f"snowsql -a {account} -u {username} -w {password}"
subprocess.run(cmd, shell=True)