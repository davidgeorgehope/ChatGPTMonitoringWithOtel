import openai
from functools import wraps
from opentelemetry import trace

counters = {'completion_count': 0, 'token_count': 0, 'prompt_tokens': 0, 'completion_tokens': 0}

def count_completion_requests_and_tokens(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        counters['completion_count'] += 1
        response = func(*args, **kwargs)
        print(response)

        token_count = response.usage.total_tokens
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        
        # Set OpenTelemetry attributes
        span = trace.get_current_span()
        if span:
            span.set_attribute("completion_count", counters['completion_count'])
            span.set_attribute("token_count", token_count)
            span.set_attribute("prompt_tokens", prompt_tokens)
            span.set_attribute("completion_tokens", completion_tokens)
            span.set_attribute("model", response.model)
        return response
    return wrapper

# Monkey-patch the openai.Completion.create function
openai.Completion.create = count_completion_requests_and_tokens(openai.Completion.create)

