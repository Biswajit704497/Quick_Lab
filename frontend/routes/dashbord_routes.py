from flask import Blueprint, render_template, redirect, url_for
dashbord_bp = Blueprint('dashbord_bp', __name__)

@dashbord_bp.route('/dashbord')
def dashbord():
    
    return render_template("dashbord.html")