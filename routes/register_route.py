from flask import Blueprint, render_template, session, redirect, url_for, request, flash
register_bp = Blueprint('register_bp',__name__)
from db_config import mysql
@register_bp.route('/register',methods=['GET','POST'])
def register():

    if 'user' in session:
        flash("Your acount already axist", "warning")
        return redirect(url_for('main_bp.home'))

    if request.method == 'POST':
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        full_name = request.form.get("full_name")
        username = request.form.get("username")
        password = request.form.get("password")

        #database connection
        user_data = (
            email,
            phone_number,
            full_name,
            username,
            password
        )
        
        sql_query = """
            INSERT INTO userlogin(email,phone_number,full_name,username,password)
            VALUES(%s, %s, %s , %s , %s )"""
        cur = None
        conn = None
        try:
            conn = mysql.connect
            cur = conn.cursor()
            cur.execute(sql_query, user_data)
            conn.commit()
            flash("Registration Successfully", "success")
            return redirect(url_for("login_bp.login"))
        except Exception :
            flash("database connection probleam","warning")
       
    return render_template('register.html')