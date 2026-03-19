from flask import Blueprint, session, redirect, url_for,flash
from authlib.integrations.flask_client import OAuth
from frontend.db_config import mysql
from frontend.module import user_id
import os

google_auth = Blueprint("google_auth", __name__)
oauth = OAuth()

@google_auth.record_once
def init_oauth(state):
    app = state.app
    oauth.init_app(app)

    oauth.register(
        name='google',
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={'scope': 'openid email profile'}
    )



@google_auth.route("/google_auth/google_login")
def google_login():
    redirect_uri = url_for("google_auth.google_callback", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@google_auth.route("/google_auth/google_login/callback")
def google_callback():

    token = oauth.google.authorize_access_token()
    user_info = oauth.google.userinfo()  # auto works with OpenID

    print(f"user information: {user_info["email"] ,user_info["name"], user_info["picture"]}" )
    userEmail = user_info.get('email')
    userFullName = user_info.get('name')
    userId = user_id.generate_user_id()
    
    
    user_data = (userId,
                 userEmail,
                 userFullName,
                 )
    
    sql_query = """INSERT INTO userlogin(userId,userEmail,userFullName) VALUES(%s,%s,%s)"""

    # send data in  Database
    try:

        db = mysql.connect
        cursor = db.cursor()
        
        #check user alreay register
        cursor.execute("SELECT userFullName, userEmail FROM userlogin WHERE userEmail=%s",(userEmail,))
        user = cursor.fetchone()

        if not user :
            cursor.execute(sql_query, user_data)
            db.commit()
            session["user"] = user_info["email"]
            flash("login Successfully", "success")
            return redirect(url_for("login_bp.login"))
        elif user:
            session["user"] = user_info["email"]
            flash("login Successfully", "success")
            return redirect(url_for("main_bp.home"))

    except Exception as e :
        print("database: ", e)
        flash("something wrong", "warning")
        return redirect(url_for("login_bp.login"))
            
    return redirect(url_for("login_bp.login"))
    



