from flask import Blueprint, render_template, session, redirect, url_for, request, flash
register_bp = Blueprint('register_bp',__name__)
from frontend.db_config import mysql
from module import user_id
from datetime import date

@register_bp.route('/register',methods=['GET','POST'])
def register():

    if 'user' in session:
        flash("Your acount already axist", "warning")
        return redirect(url_for('main_bp.home'))

    if request.method == 'POST':

        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        full_name = request.form.get("full_name")
        password = request.form.get("password") 
        confirm_password = request.form.get("confirmpassword")
        created_at = date.today()
        user_ID = user_id.generate_user_id()

        if ( confirm_password!=password ):
            return redirect("/register")

        #database connection
        user_data = (
            user_ID,
            full_name,
            phone_number,
            password,   
            created_at,  
            email
        )
        print(user_data)
        sql_query = """
            INSERT INTO userlogin(userID,userFullName,userPHNumber,userPassword,userJoinDate, userEmail)
            VALUES(%s, %s, %s , %s , %s, %s )"""
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