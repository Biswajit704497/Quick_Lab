from flask import Blueprint,render_template,url_for,flash, redirect,session
import MySQLdb.cursors
profile_bp = Blueprint('profile_bp', __name__)
from db_config import mysql
@profile_bp.route('/profile')
def profile():
    
    if "user" not in session:
        flash("Please login first","warning")
        return redirect(url_for("main_bp.home"))
    
    username = session["user"]
    print(session["user"])
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM userlogin WHERE username=%s", (username,))
    user_data = cur.fetchone()
    cur.close()
    return render_template("profile.html", user = user_data)