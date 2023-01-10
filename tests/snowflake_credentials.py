import subprocess
import os

#setting variables based upon the windows global variables.

account = os.getenv('snowflake_account')
username = os.getenv('snowflake_username')
password = os.getenv('snowflake_password')

print('Variables for login are as follows:')
print('Account:' + account)
print('Username:' + username)
print('Password:' + password)
