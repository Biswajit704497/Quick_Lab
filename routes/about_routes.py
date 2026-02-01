from flask import Blueprint, render_template, redirect, url_for
about_bp = Blueprint('about_bp',__name__)

@about_bp.route('/about')
def about_page():

    return render_template('about.html')