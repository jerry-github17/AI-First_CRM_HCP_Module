# from fastapi import FastAPI

# app = FastAPI(title="AI-First CRM API")


# @app.get("/")
# def root():
#     return {"message": "AI-First CRM backend is running"}

#continuation

# from fastapi import FastAPI
# from .database import engine
# from .models import Base

# Base.metadata.create_all(bind=engine)

# app = FastAPI(title="AI-First CRM API")


# @app.get("/")
# def root():
#     return {
#         "message": "AI-First CRM backend is running"
#     }
# Continuation2

from fastapi import FastAPI 
from .routers import chat
from .database import engine
from .models import Base
from .routers import interactions
from fastapi.middleware.cors import CORSMiddleware  #the ports of fast api and react front end are differend

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI-First CRM API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    interactions.router
)
#added while connecting to langgraph
app.include_router(
    chat.router
)

@app.get("/")
def root():

    return {
        "message": "AI-First CRM backend is running"
    }