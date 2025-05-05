from fastapi import FastAPI
from routers import auth, analyze, user, recommend

app = FastAPI(title="FURIA Fan Analyzer")

app.include_router(auth.router)
app.include_router(analyze.router)
app.include_router(user.router)
app.include_router(recommend.router)

@app.get("/")
def read_root():
    return {"message": "FURIA Fan Analyzer API is running"}