import os
import login 
get_user=input("Enter username\n")
get_pass=input("\nenter password\n")
def save(get_user,get_pass):
    with open(".env","w") as f:
        f.write(f"username={get_user}\n")
        f.write(f"password={get_pass}")
        f.close
save(get_user,get_pass)
if login.login():
    print("succesfull")
else:
    print("login failed")