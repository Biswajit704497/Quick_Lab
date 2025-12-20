from flask import Blueprint, flash, redirect, url_for, session, render_template,request,Response
cancer_bp = Blueprint('cancer_bp',__name__)
from models.cancer_model import cancer_fun

@cancer_bp.route("/cancer_route", methods = ["GET", "POST"])
def cancer():
    result = None
    if "user" not in session:
        flash("please login first to access", "warning")
        return redirect(url_for("login_bp.login"))
   
    if request.method == 'POST':
        radius_mean = float(request.form.get('radius_mean', 0))
        texture_mean = float(request.form.get('texture_mean', 0))
        perimeter_mean = float(request.form.get('perimeter_mean',0))
        area_mean = float(request.form.get('area_mean',0))
        smoothness_mean = float(request.form.get('smoothness_mean', 0))
        compactness_mean = float(request.form.get('compactness_mean',0))
        concavity_mean = float(request.form.get('concavity_mean', 0))
        concave_points_mean =float(request.form.get('concave_points_mean', 0))
        
        print(radius_mean,texture_mean,perimeter_mean,area_mean, smoothness_mean,compactness_mean,concavity_mean,concave_points_mean )
        user_data = [radius_mean,texture_mean,perimeter_mean,area_mean, smoothness_mean,compactness_mean,concavity_mean,concave_points_mean]
        result = cancer_fun(user_data)
    return render_template("cancer.html", result = result)

