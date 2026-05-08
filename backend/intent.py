from .utils import call_llm

INTENT_PROMPT = """
Extract the following from the user request as JSON:
{
  "features": ["list of main features"],
  "entities": ["list of data entities (e.g., User, Contact, Order)"],
  "roles": ["list of user roles (e.g., admin, member, guest)"],
  "constraints": ["any special rules or limitations"]
}

User request: {prompt}
"""

def extract_intent(user_prompt: str) -> dict:
    prompt = INTENT_PROMPT.format(prompt=user_prompt)

    result = call_llm(
        prompt,
        temperature=0
    )

    return result