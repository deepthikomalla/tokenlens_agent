from fastapi import FastAPI
from groq import Groq
from dotenv import load_dotenv
import os

from tokenlens import observe, LatencyTracker

load_dotenv()

app = FastAPI()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

@app.get("/")
def home():
    return {
        "message": "TokenLens AI Agent Running"
    }

@app.post("/chat")
def chat(query: str):

    timer = LatencyTracker()
    timer.start()

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )

    latency = timer.stop()

    metrics = observe(response, latency)

    return {
        "response": response.choices[0].message.content,
        "metrics": metrics
    }