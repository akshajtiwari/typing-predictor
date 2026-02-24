import pandas as pd
import joblib
import os
from sqlalchemy import create_engine
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

engine = create_engine("postgresql+psycopg2://postgres@localhost/postgres")


def train_and_predict(username):

    # get user_id
    q = f"SELECT id FROM users WHERE username='{username}'"
    user_df = pd.read_sql(q, engine)

    if user_df.empty:
        print("User not found in DB")
        return

    user_id = user_df["id"].iloc[0]

    # fetch typing data
    q = f"""
    SELECT test_time, wpm 
    FROM typing_tests 
    WHERE user_id={user_id}
    ORDER BY test_time
    """
    df = pd.read_sql(q, engine)

    if len(df) < 30:
        print("Not enough data to train model")
        return

    df["test_time"] = pd.to_datetime(df["test_time"])
    df["days"] = (df["test_time"] - df["test_time"].min()).dt.days

    X = df[["days"]]
    y = df["wpm"]

    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)

    model = LinearRegression()
    model.fit(X_poly, y)

    os.makedirs("models", exist_ok=True)
    joblib.dump((model, poly), f"models/{username}.pkl")

    print("Model trained")

    # predict 180 days future
    last_day = df["days"].max()
    future_day = last_day + 180

    future_df = pd.DataFrame([[future_day]], columns=["days"])
    future_poly = poly.transform(future_df)

    pred = model.predict(future_poly)[0]

    print(f"\n Predicted typing speed after 6 months: {round(pred,2)} WPM\n")
