import joblib
model = joblib.load('C:\\Users\\ytsub\\Desktop\\github\\Know_Your_Health_MLModel\\models\\cancer.pkl')

def cancer_fun(data):
    predict = model.predict([data])
    return predict
