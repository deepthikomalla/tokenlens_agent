from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

from tokenlens import (
    capture_tokens,
    log_tokens
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# Tool required by PDF
def calculator(expression: str):
    return str(eval(expression))


def run_agent(query: str):

    if query.startswith("calc:"):

        result = calculator(
            query.replace(
                "calc:",
                ""
            )
        )

        return {
            "response": result,
            "tool": "calculator"
        }

    response = llm.invoke(query)

    tokens = capture_tokens(
        response
    )

    log_tokens(tokens)

    return {
        "response": response.content,
        "tokens": tokens
    }