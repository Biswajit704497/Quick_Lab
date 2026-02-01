from flask import Blueprint, session, redirect, url_for,flash
from authlib.integrations.flask_client import OAuth
from db_config import mysql
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
    email = user_info.get('email')
    full_name = user_info.get('name')
    username = full_name


    print(f"user information: {user_info['email'] ,user_info['name'], user_info['picture']}" )
    
    user_data = (email,
                 full_name,
                 username )
    sql_query = """ INSERT INTO userlogin(email,full_name, username) VALUES(%s,%s,%s)"""

    # send data in  Database
    try:

        db = mysql.connect
        cursor = db.cursor()
        
        #check user alreay register
        cursor.execute(
            "SELECT full_name FROM userlogin WHERE email=%s",
            (email,)
        )
        user = cursor.fetchone()

        if not user :
            print(user)
            cursor.execute(sql_query, user_data)
            
            db.commit()
            session["user"] = user_info["email"]
            db.close()
            cursor.close()
        
        flash("login Successfully", "success")
        return redirect(url_for("login_bp.login"))
    
    except Exception as e :
        print("database: ", e)
        flash("something wrong", "warning")
        return redirect(url_for("login_bp.login"))
            

    # return redirect(url_for("main_bp.home"))


