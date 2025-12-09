from flask import Blueprint, session, redirect, url_for
from authlib.integrations.flask_client import OAuth
import os
import requests

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
    session["user"] = user_info["email"]
    session["name"] = user_info["name"]
    return redirect(url_for("main_bp.home"))


