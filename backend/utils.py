import openai
import json
import time

client = openai.OpenAI()

def call_llm(prompt: str, temperature: float = 0.0, max_tokens: int = 2000):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or gpt-3.5-turbo for lower cost
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
        response_format={"type": "json_object"}  # enforces JSON
    )
    return response.choices[0].message.content