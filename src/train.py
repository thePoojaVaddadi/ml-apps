import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train():
    # load YOUR dataset
    data = pd.read_csv("data/house_price_dataset.csv")

    X = data[["size", "bedrooms", "age"]]
    y = data["price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=150,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print("Model R2 Score:", score)

    # save model
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("✅ Model saved to models/model.pkl")

if __name__ == "__main__":
    train()