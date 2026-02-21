from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__)

@main_bp.route("/")
def home():
    
    return render_template("home.html")

@main_bp.route("/help_page")
def help():
    return render_template('helppage.html')

@main_bp.route("/about")
def about_page():

    return render_template('about.html')


