from .intent import extract_intent
from .design import design_system
from .schema_gen import generate_schemas
from .validation import validate_and_repair

def run_pipeline(prompt: str) -> dict:
    intent = extract_intent(prompt)
    if is_vague(intent):
        return {"status": "needs_clarification", "questions": ["What are the main entities?", "Who are the users?"]}
    # ... rest of pipeline

def run_pipeline(user_prompt: str) -> dict:
    # Stage 1
    intent = extract_intent(user_prompt)
    # Stage 2
    design = design_system(intent)
    # Stage 3
    schemas = generate_schemas(design)
    # Stage 4: repair each layer
    final_config = {
        "db_schema": validate_and_repair(schemas["db_schema"], "db"),
        "api_config": validate_and_repair(schemas["api_config"], "api"),
        "ui_config": validate_and_repair(schemas["ui_config"], "ui"),
        "auth_config": validate_and_repair(schemas["auth_config"], "auth"),
    }
    return final_config