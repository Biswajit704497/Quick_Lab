from flask import Blueprint, session, redirect, url_for, flash
from authlib.integrations.flask_client import OAuth
from frontend.db_config import mysql
from frontend.module import user_id
import os

google_auth = Blueprint("google_auth", __name__, url_prefix="/google_auth")
oauth = OAuth()

@google_auth.record_once
def init_oauth(state):
    app = state.app
    os.environ.setdefault("OAUTHLIB_INSECURE_TRANSPORT", "1")
    oauth.init_app(app)

    oauth.register(
        name='google',
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={'scope': 'openid email profile'}
    )

@google_auth.route("/google_login")
def google_login():
    try:
        redirect_uri = os.getenv("GOOGLE_REDIRECT_URI", url_for("google_auth.google_callback", _external=True))
        print(f"Using Google redirect URI: {redirect_uri}")
        return oauth.google.authorize_redirect(redirect_uri)
    
    except Exception as e:
        print(f"Google login error: {e}")
        flash("Network error", "error")
        return redirect(url_for("login_bp.login"))


@google_auth.route("/google_login/callback")
def google_callback():

    token = oauth.google.authorize_access_token()
    user_info = oauth.google.userinfo()  # auto works with OpenID

    print(f"user information: {user_info.get('email')}, {user_info.get('name')}, {user_info.get('picture')}")
    userEmail = user_info.get('email')
    userFullName = user_info.get('name')
    userId = user_id.generate_user_id()
    
    user_data = (userId,
                 userEmail,
                 userFullName,
                 )
    
    sql_query = """INSERT INTO userLogin(id,email,name) VALUES(%s,%s,%s)"""

    # send data in  Database
    try:

        db = mysql.connect
        cursor = db.cursor()
        
        #check user alreay register
        cursor.execute("SELECT name, email FROM UserLogin WHERE email=%s",(userEmail,))
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
    



