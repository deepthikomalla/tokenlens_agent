# tokenlens/tracker.py

from .token_counter import get_token_usage

def observe(response, latency):
    usage = get_token_usage(response)

    return {
        "prompt_tokens": usage["prompt_tokens"],
        "completion_tokens": usage["completion_tokens"],
        "total_tokens": usage["total_tokens"],
        "latency_seconds": latency
    }