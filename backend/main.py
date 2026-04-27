from fastapi import FastAPI, Query, Path
from routes import ecg_routes
app = FastAPI()


@app.get('/')
def home_api():
    return {"ditals": "wellcome Quick Lab API service",
            "devloped by": "YT subhadip",
            "project": "Qick Lab"
            }

app.include_router(ecg_routes.route, prefix="/api/v1")



