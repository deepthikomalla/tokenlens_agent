def capture_tokens(response):

    usage = response.response_metadata.get(
        "token_usage",
        {}
    )

    return {
        "prompt_tokens": usage.get(
            "prompt_tokens",
            0
        ),
        "completion_tokens": usage.get(
            "completion_tokens",
            0
        ),
        "total_tokens": usage.get(
            "total_tokens",
            0
        )
    }