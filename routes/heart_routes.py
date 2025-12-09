from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from models.heart_model import heart_def

heart_bp = Blueprint('heart_bp', __name__)

@heart_bp.route("/heart_attack", methods=['GET', 'POST'])
def heart_attack():
    user_data=[]
    result = None
    if 'user' not in session:
        flash('Please log in first to access.', 'warning')
        return redirect(url_for('login_bp.login'))
    
    if request.method == 'POST':
        age = int(request.form.get('age',0))
        gender = int(request.form.get('gender', 0))
        highBloodPressure =int(request.form.get('highBloodPressure',0))
        lowBloodPressure = int(request.form.get('lowBloodPressure', 0))
        cholesterol = int(request.form.get('cholesterol',0))
        heartRate = int(request.form.get('heartRate', 0))
        smoking = int(request.form.get('smoking', 0))
        alcoholConsumption = int(request.form.get('alcoholConsumption', 0))
        exerciseHours = int(request.form.get('exerciseHours', 0))
        diet = int(request.form.get('diet', 0))
        diabetes = int(request.form.get('diabetes',0))
        familyHistory = int(request.form.get('familyHistory', 0))
        previousHeartProblems =int(request.form.get('previousHeartProblems', 0))
        medicationUse = int(request.form.get('medicationUse', 0))
        stressLevel = int(request.form.get('stressLevel', 0))

        user_data = [age, gender, highBloodPressure, lowBloodPressure,cholesterol, heartRate, smoking, alcoholConsumption, exerciseHours, diet, diabetes, familyHistory, previousHeartProblems, medicationUse, stressLevel]
        print(user_data)

        
        
        # call heart attack function
        prediction = heart_def([user_data])
        result = "High Risk of Heart Attack" if prediction[0] == 1 else "Low Risk of Heart Attack"
        
    
    return render_template("heart.html", result = result)
