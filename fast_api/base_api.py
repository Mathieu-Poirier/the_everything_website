from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

server = FastAPI()

origins = [

    "http://localhost",
    "*"
        ]

server.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@server.get("/healthcheck")
def health_check():
    return {"message": "API healthcheck works"}

@server.get("/")
def health_check():
    return {"message": "Welcome to the home route!"}

@server.post("/button")
def increment_value(value: int):
    return value + 1
