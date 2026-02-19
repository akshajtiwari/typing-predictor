#  BFORE COPYING CREATE A NEW COLUMN IN THE DF SAME AS THE USER ID ...NAME WILL BE user_id ....AND THEN REORDER THE DF TO MATCH THE DB SCHEMA

import pandas as pd
import preprocess
import os
import psycopg2 as postgre
from dotenv import load_dotenv
import preprocess
from sqlalchemy import create_engine
load_dotenv()

username = os.getenv("db_username")

conn = postgre.connect("dbname=postgres user=postgres")
cur = conn.cursor()

cur.execute("SELECT id,username FROM users")
users = cur.fetchall()

user_dict = {u[1]: u[0] for u in users}   # {username: id}

if username in user_dict:
    print(f"user {username} exists")
    user_id = user_dict[username]

else:
    print("user does not exist")
    try:
        sql = "INSERT INTO users(username) VALUES (%s) RETURNING id"
        data=(username,) # create a single tuple using comma
        cur.execute(sql, data)
        user_id = cur.fetchone()[0]   # get inserted user id from the db
        conn.commit()

        print(f"user {username} inserted successfully with id {user_id}")

    except Exception as e:
        print(e)
        conn.rollback()

df = preprocess.processed_df.copy()


df["user_id"] = user_id # create new column with SAME user id for all rows

# reorder dataframe to match DB schema
final_processed_df = df[
    [
        "user_id",
        "test_time",
        "wpm",
        "raw_wpm",
        "accuracy",
        "consistency",
        "correct_chars",
        "incorrect_chars",
        "extra_chars",
        "missed_chars",
        "test_duration",
        "mode",
        "mode2",
        "quote_length",
        "language",
        "difficulty",
        "is_pb",
        "punctuation",
        "numbers",
    ]
]
engine = create_engine("postgresql+psycopg2://postgres@localhost/postgres") # for copying the dataframe to the table 

# append into table
final_processed_df.to_sql(
    "typing_tests",
    con=engine,
    if_exists='append',
    index=False
)

print("Data inserted successfully.")
try:
    final_processed_df.to_csv("processed_data/processed_data.csv")
    print("processed csv saved sucessfully")
except Exception as e:
    print(e)
#close the db
# cur.close()
# conn.close()