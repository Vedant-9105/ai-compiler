import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def call_llm(
    prompt: str,
    temperature: float = 0.0,
    max_tokens: int = 2000
):

    response = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=temperature,
        max_tokens=max_tokens,

        response_format={
            "type": "json_object"
        }
    )

    # Convert JSON string -> Python dict
    return json.loads(
        response.choices[0].message.content
    )