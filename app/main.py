from fastapi import FastAPI
from app.routes import user,auth,document,ingestion
#, document, 

app = FastAPI()

#sRegister route modules
app.include_router(user.router, prefix="/users", tags=["User Management"])
app.include_router(auth.router, prefix="/login", tags=["Authentication"])
app.include_router(document.router, prefix="/documents", tags=["Document Management"])
app.include_router(ingestion.router, prefix="/ingestion", tags=["Ingestion Management"])

@app.get("/")
def root():
    return {"message": "Backend is up and running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
