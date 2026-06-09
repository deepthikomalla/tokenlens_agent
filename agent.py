from groq import Groq
from dotenv import load_dotenv
import os

from tokenlens import observe, log_tokens, LatencyTracker

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Example tool
def calculator(expression: str):
    return str(eval(expression))

def run_agent(query: str):

    timer = LatencyTracker()
    timer.start()

    # Simple tool usage
    if query.startswith("calc:"):
        result = calculator(query.replace("calc:", "").strip())

        return {
            "response": result,
            "metrics": {
                "tool_used": "calculator"
            }
        }

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

    log_tokens(metrics)

    return {
        "response": response.choices[0].message.content,
        "metrics": metrics
    }