from fastapi import FastAPI
from app.routes import user,auth,document,ingestion
from app.middleWare.combined import CombinedMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#for rexposing new token
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-New-Token"]
)

# custom middleware
app.add_middleware(CombinedMiddleware)

#Register route modules
app.include_router(user.router, prefix="/users", tags=["User Management"])
app.include_router(auth.router, prefix="/login", tags=["Authentication"])
app.include_router(document.router, prefix="/documents", tags=["Document Management"])
app.include_router(ingestion.router, prefix="/ingestion", tags=["Ingestion Management"])

@app.get("/")
def root():
    return {"message": "Backend is up and running!"}
