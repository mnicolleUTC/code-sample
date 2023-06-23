import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline



if __name__ == '__main__':
    file = './input_data/profile_member_vs_non_member.csv'
    df = pd.read_csv(file)
    df["age"]=df["age"].apply(lambda x: int(x))
    df["income"]= df["income"].apply(lambda x: int(x))
    df['member'] = df['member'].fillna(0)
    df['age'] = df['age'].astype(int)
    df['income'] = df['income'].astype(int)
    df['member'] = df['member'].astype(int)
    print(df.tail())
    print(df["member"].unique())
    # Define preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['age', 'income']),
            ('cat', OneHotEncoder(), ['gender'])
        ])

    # Define your model
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

    # Create a pipeline that preprocesses the data and then trains the model
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                            ('model', model)])

    # Define your X and y
    X = df[['gender', 'age', 'income']]
    y = df['member']

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fit the model
    pipeline.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = pipeline.predict(X_test)

    # Check accuracy on the test data
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy*100}%')