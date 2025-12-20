from flask import Blueprint, render_template, session, redirect,url_for, request, flash
from db_config import mysql
login_bp = Blueprint('login_bp',__name__)

@login_bp.route('/login', methods=['GET','POST'])
def login():
    # if user is already logged in, redirect to home
    if "user" in session:
        flash("You are already logged in.", "success")
        return redirect(url_for('main_bp.home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cur = None
        try:

            cur = mysql.connect.cursor()
            cur.execute("SELECT * FROM userlogin WHERE username=%s AND password=%s", (username, password))
            user = cur.fetchone()
            
            # print("database reply",user)
            
            if user:
                session["user"] = username
                flash("Login successful!", "success")
                return redirect(url_for('main_bp.home'))
            else:
                flash("Invalid username or password", "danger")

        except Exception as e:
            flash("Database connection problem: " + str(e), "error")

        finally:
            if cur:
                cur.close()
    return render_template('login.html')    




@login_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logout...... ", "success")
    return redirect(url_for('main_bp.home'))


