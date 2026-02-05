from flask import Blueprint, render_template, request, session,flash,redirect,url_for
from module.bmi_calculate import BMI_def

bmi_bp = Blueprint('bmi_bp', __name__)

@bmi_bp.route("/bmi_route", methods=['GET', 'POST'])
def bmi():
    if 'user' not in session:
        print(True)
        flash('Please log in first to access BMI calculator.', 'warning')
        return redirect(url_for('login_bp.login'))

    person_bmi = None
    if request.method == 'POST':
        weight = int(request.form.get('weight', 0))
        height = int(request.form.get('height', 0))
        person_bmi = BMI_def(height, weight)

    return render_template('bmi.html', person_bmi=person_bmi)
