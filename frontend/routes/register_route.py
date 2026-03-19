from flask import Blueprint, render_template, session, redirect, url_for, request, flash
register_bp = Blueprint('register_bp',__name__)
from frontend.db_config import mysql
from frontend.module import user_id
from datetime import date

@register_bp.route('/register',methods=['GET','POST'])
def register():

    if 'user' in session:
        flash("Your acount already axist", "warning")
        return redirect(url_for('main_bp.home'))

    if request.method == 'POST':

        email = request.form.get("email")
        full_name = request.form.get("full_name")
        password = request.form.get("password") 
        created_at = date.today()
        user_ID = user_id.generate_user_id()

        # input validation
        fields = [email, full_name, password]
        if any(not field.strip() for field in fields):
            flash("all field are requird","error")
            return redirect(url_for("register_bp.register"  ))

       
      
       
        try:
            # check user already exist
            conn = mysql.connect 
            cur = conn.cursor()
            cur.execute("select * from userlogin where userEmail = %s", (email,))
            data = cur.fetchone()

            if data:
                flash("user already save in database","warning")  
                return redirect(url_for("login_bp.login"))  
             
            # insert data in database
            sql_query = """
            INSERT INTO userlogin(userID,userFullName,userPassword,userJoinDate, userEmail)
            VALUES(%s, %s, %s , %s , %s)
            """
            user_data = (
                user_ID,
                full_name,
                password,   
                created_at,  
                email)
        
            try:
                cur.execute(sql_query, user_data)
                conn.commit()
                flash("Registration Successfully", "success")
                return redirect(url_for("login_bp.login"))
            
            except Exception as e :
                print(e)
                flash(f"database connection probleam","warning")

        except Exception as e:
            print(e)
            flash(f"Data base error","error")
        
       
       
       
    return render_template('register.html')