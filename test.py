#imports
import os 
import subprocess
import psutil
default_secure_password = "T0tallyS3curePASSWORD!1!!"
input("WARNING! COMPLETE ALL FORENSICS BEFORE RUNNING! Press enter to confirm.")
auth_users = []
auth_admins = []
os.system('net user > users.txt')
user_list = psutil.users()
print(user_list)


#getting valid users
while(True):
	append_user = input("Input a valid non admin user, one at a time \n(Press enter once to stop inputting users): ")
	if not append_user in auth_users:
		auth_users.append(append_user)
	else:
		print("Already a user")
	if(auth_users[-1] == ""):
		auth_users = auth_users[:-1]
		break
print("Same thing for admins")
while(True):
	append_user = input("Input a valid admin, one at a time \n(Press enter once to stop inputting users): ")
	if not append_user in auth_admins:
		auth_admins.append(append_user)
	else:
		print("already an admin")
	if(auth_admins[-1] == ""):
		auth_admins = auth_admins[:-1]
		break


#Disable built in guest + admin account
os.system("net user Guest /active no")
os.system("net user Administrator /active no")


#TODO: Delete users not in the valid users pool
for p in user_list:
  if p.name not in auth_users or p.name not in auth_admins:
    #remove the thing xd
    print("Removed " + p.name + " from life")
    os.system("net user" + p.name  + "/Delete")
  else:
      print(p.name + " is a good boy :)")
