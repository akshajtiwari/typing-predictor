import pandas as pd
import joblib
import os
from sqlalchemy import create_engine
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

engine = create_engine("postgresql+psycopg2://postgres@localhost/postgres")


def evaluate(username):

    model_path = f"models/{username}.pkl"

    if not os.path.exists(model_path):
        print("Model file not found.")
        return

    # Load model and polynomial transformer
    model, poly = joblib.load(model_path)

    # Fetch data
    query = f"""
    SELECT test_time, wpm 
    FROM typing_tests t
    JOIN users u ON t.user_id = u.id
    WHERE u.username = '{username}'
    ORDER BY test_time
    """

    df = pd.read_sql(query, engine)

    if len(df) < 30:
        print("Not enough data for evaluation.")
        return

    df["test_time"] = pd.to_datetime(df["test_time"])
    df["days"] = (df["test_time"] - df["test_time"].min()).dt.days

    X = df[["days"]]
    y = df["wpm"]

    # 80/20 split (time-aware split, no shuffle)
    split_index = int(len(df) * 0.8)

    X_train = X.iloc[:split_index]
    y_train = y.iloc[:split_index]

    X_test = X.iloc[split_index:]
    y_test = y.iloc[split_index:]

    # Transform
    X_train_poly = poly.transform(X_train)
    X_test_poly = poly.transform(X_test)

    # Predictions
    y_train_pred = model.predict(X_train_poly)
    y_test_pred = model.predict(X_test_poly)

    # Metrics
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)

    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)

    print("\nModel Evaluation Results\n")
    print(f"Train R²: {round(train_r2, 4)}")
    print(f"Test  R²: {round(test_r2, 4)}\n")

    print(f"Train MSE: {round(train_mse, 4)}")
    print(f"Test  MSE: {round(test_mse, 4)}\n")

    # Overfitting check
    if train_r2 - test_r2 > 0.15:
        print("⚠️ Model may be overfitting.")
    else:
        print("✅ No major overfitting detected.")


if __name__ == "__main__":
    username = input("Enter username to evaluate: ")
    evaluate(username)