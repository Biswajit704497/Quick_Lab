from flask import Blueprint, render_template, flash, redirect, url_for, session, request
from models.diabetes_model import diabetes_fun
diabetes_bp = Blueprint('diabetes_bp',__name__)

@diabetes_bp.route("/diabetes", methods = ['GET', 'POST'])
def diabetes():
    if 'user' not in session:
        flash("please login first to access", "warning")
        return redirect(url_for('login_bp.login'))
    
    if request.method == 'POST':
        Pregnancies = request.form.get('Pregnancies',0)
        Glucose = request.form.get('Glucose',0)
        BloodPressure = request.form.get('BloodPressure',0)
        SkinThickness = request.form.get('SkinThickness', 0)
        Insulin = request.form.get('Insulin', 0)
        bmi = request.form.get('bmi', 0)
        DiabetesPedigreeFunction =request.form.get('dpf',0)
        Age = request.form.get('Age', 0)
        data  = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, bmi, DiabetesPedigreeFunction, Age]
        result = diabetes_fun(data)
        
    return render_template("diabetes.html", result = result)

