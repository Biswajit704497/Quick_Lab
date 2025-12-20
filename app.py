from flask import Flask
# from db_config import mysql,init_db 
from routes.main_routes import main_bp
from routes.bmi_routes import bmi_bp
from routes.heart_routes import heart_bp
from routes.login_routes import login_bp
from routes.register_route import register_bp
from routes.diabetes_routes import diabetes_bp
from routes.user_profile import profile_bp
from routes.google_auth import google_auth
from routes.cancer_routes import cancer_bp
from routes.chatbot_route import chatbot_bp
import os
import requests
from flask_cors import CORS



from db_config import init_mysql

app = Flask(__name__,static_folder='static')
app.secret_key = "asasacddf1f2d15f4d5f5d4f55454212143@d4s5d4as" 

CORS(app)

# init_db(app)
mysql = init_mysql(app)
# Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(heart_bp)
app.register_blueprint(bmi_bp)
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(diabetes_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(google_auth)
app.register_blueprint(cancer_bp)
app.register_blueprint(chatbot_bp)

@app.route("/db_test")
def db_test():
    cur = mysql.connection.cursor()
    cur.execute("SELECT 1")
    data = cur.fetchone()
    return f"Database OK: {data}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
