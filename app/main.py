from fastapi import FastAPI
from app.routes import user,auth,document,ingestion
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",  # Angular dev server
    # Add any other allowed frontend domains here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # use ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],  # or ["POST", "GET", "OPTIONS"] as needed
    allow_headers=["*"],
)

#sRegister route modules
app.include_router(user.router, prefix="/users", tags=["User Management"])
app.include_router(auth.router, prefix="/login", tags=["Authentication"])
app.include_router(document.router, prefix="/documents", tags=["Document Management"])
app.include_router(ingestion.router, prefix="/ingestion", tags=["Ingestion Management"])

@app.get("/")
def root():
    return {"message": "Backend is up and running!"}
