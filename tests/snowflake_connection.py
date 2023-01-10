import subprocess
import os

#setting variables based upon the windows global variables. Global variables setup outside of this codebase.
#account = os.getenv('snowflake_account')
#username = os.getenv('snowflake_username')
#password = os.getenv('snowflake_password')

#snowsql executable which will be used
#snow_path = "C:\Program Files\Snowflake SnowSQL\snowsql.exe"

#login command
#command = [snow_path,"-a",account,"-u",username,"-w",password]

#execute command
#subprocess.run(command)

command = "snowsql -c newConnection"
subprocess.run(command)