from models import cursos_model
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import engine

cursos_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/cursos")
def root():
    return {"message": "Welcome to FastAPI of Cursos"}
    