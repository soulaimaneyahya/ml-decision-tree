import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


def main():
    # Convert data to DataFrame
    df = pd.read_csv("./data/data.csv")

    # Map categorical variables to numerical values
    d = {'Female': 0, 'Male': 1}
    df['Gender'] = df['Gender'].map(d)
    d = {'Yes': 1, 'No': 0}
    df['Purchase'] = df['Purchase'].map(d)

    # Define features and target variable
    features = ['Age', 'Gender', 'Income']
    X = df[features]
    Y = df['Purchase']

    # Train Decision Tree Classifier
    dtree = DecisionTreeClassifier()
    dtree = dtree.fit(X, Y)

    # Predict
    input_data = pd.DataFrame([[50, 1, 50000]], columns=features)
    prediction = dtree.predict(input_data)
    print("Prediction:", prediction)

    print("[1] means 'Yes'")
    print("[0] means 'No'")

if __name__ == "__main__":
    main()
