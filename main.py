import os
import time
from dotenv import load_dotenv
import login

ENV_FILE = ".env"



# READ EXISTING ENV USER

def get_saved_username():
    if not os.path.exists(ENV_FILE):
        return None

    load_dotenv()
    return os.getenv("username")



# SAVE NEW CREDENTIALS

def save_credentials():
    user = input("Enter Monkeytype username/email:\n")
    pwd = input("Enter Monkeytype password:\n")
    db_user = input("Enter DB username label (any name):\n")

    with open(ENV_FILE, "w") as f:
        f.write(f"username={user}\n")
        f.write(f"password={pwd}\n")
        f.write(f"db_username={db_user}\n")

    print("Credentials saved\n")



# CHECK USER

saved_user = get_saved_username()

if saved_user:
    print(f"Saved user found: {saved_user}")
    choice = input("Use same user? (y/n): ").lower()

    if choice == "n":
        save_credentials()
        load_dotenv()
        need_login = True
    else:
        load_dotenv()
        need_login = False
else:
    save_credentials()
    load_dotenv()
    need_login = True



# LOGIN OR SKIP

print("\nStarting browser...\n")

if need_login:
    print("Logging in...")
    if not login.login():
        print("Login failed")
        exit()
else:
    print("Skipping login, using existing session")

# Always download CSV
if login.download_csv():
    print("CSV download triggered\n")
else:
    print("CSV download failed")
    exit()



# WAIT FOR CSV

download_folder = "/home/akshajtiwari/Desktop/typing_predictor/downloaded_files"

csv_file = None
for i in range(30):
    for f in os.listdir(download_folder):
        if f.endswith(".csv"):
            csv_file = os.path.join(download_folder, f)
            break
    if csv_file:
        break
    time.sleep(1)

if not csv_file:
    print("CSV not found")
    exit()

print("CSV found:", csv_file)



# MOVE CSV TO RAW DATA

raw_path = "/home/akshajtiwari/Desktop/typing_predictor/raw_data/results.csv"
os.replace(csv_file, raw_path)
print("CSV moved to raw_data\n")



# INSERT INTO DB

print("Processing + inserting into DB...\n")
import insert_db
print("DB insertion complete\n")



# TRAIN + PREDICT

import model

username = os.getenv("db_username")
print("Training model...\n")
model.train_and_predict(username)

print("\n FULL PIPELINE COMPLETE\n")