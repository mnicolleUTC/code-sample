
import joblib
import requests
import numpy as np

#Loading model
print("Loading model ...")
model_path = '/Users/nicollemathieu/SandBOX/code-sample/input_data/house_prices_model.joblib'
model=joblib.load(model_path)
print("model loaded!")
#Loading data
headers = {
    'accept': 'application/json',
}

response = requests.get('https://house-prices-simple-api.herokuapp.com/data', headers=headers)
string_rep = response.json()
#Formatting data into response
dict_rep = eval(string_rep)
data_full = dict_rep["data"][0]
x_test = np.array(data_full[:-1]).reshape(1,-1)
y_test = data_full[-1]
print("Using model to make prediction...")
prediction=model.predict(x_test)
print(f"According to our model, this house should cost: {prediction}")
#Comparing prediction to real value
print("Checking accuracy...")
print(f"House actual price is: {y_test}")
print(f"Our model is {prediction - y_test} away from the truth!")

