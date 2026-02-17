import os
import login 
def save():
    get_user=input("Enter username\n")
    get_pass=input("\nenter password\n")
    with open(".env","w") as f:
        f.write(f"username={get_user}\n")
        f.write(f"password={get_pass}")
        f.close()
# save()
try:
    
    if(login.login()):
        pass
        if login.download_csv():
            print("on the accounts page ")
        else:
            print("login was unsucessfull")
    else:
        print("unsuccessfull")
except Exception as e:
    print(e)
#check downloaded file
directory_name=r'/home/akshajtiwari/Desktop/typing_predictor/downloaded_files'
extensions=(".csv")
for files in os.listdir(directory_name):
    if files.endswith(extensions):
        print("csv file found")
    else:
        print("file do not exist")