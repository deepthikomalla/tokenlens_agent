from fastapi import FastAPI

from agent import run_agent

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "TokenLens AI Agent Running"
    }


@app.post("/chat")
def chat(query: str):

    return run_agent(query)