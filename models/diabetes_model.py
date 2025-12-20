import joblib

model = joblib.load("C:\\Users\\ytsub\\Desktop\\github\\Know_Your_Health_MLModel\\models\\diabetes.joblib")
def diabetes_fun(data):
    result = model.predict([data])
    return result
