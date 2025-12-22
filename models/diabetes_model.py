import joblib
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, "diabetes.joblib")

model = joblib.load(path)
def diabetes_fun(data):
    result = model.predict([data])
    return result
