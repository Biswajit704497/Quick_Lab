from fastapi import FastAPI, Query, Path
app = FastAPI()

@app.get('/')
def home_api():
    return {"ditals": "this is helth model API"}

