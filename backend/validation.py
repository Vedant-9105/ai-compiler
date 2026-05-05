import jsonschema
from . import models

def validate_and_repair(config: dict, layer: str) -> dict:
    # 1. Fix JSON syntax
    config = repair_json_syntax(config)
    
    # 2. Validate against Pydantic models (by layer)
    try:
        if layer == "db":
            models.DBConfig(**config)
        elif layer == "api":
            models.APIConfig(**config)
        # ... etc
    except Exception as e:
        # 3. Auto‑repair missing fields
        config = fill_missing_fields(config, layer)
        # 4. Cross‑layer consistency
        config = resolve_cross_layer(config)
        # 5. If still invalid, re‑generate this layer
        if not is_valid(config, layer):
            config = regenerate_layer(layer, context)
    return config

def resolve_cross_layer(config: dict) -> dict:
    # Example: API fields must exist in DB
    for endpoint in config["api_config"]:
        for field in endpoint["fields"]:
            if field not in config["db_schema"][endpoint["entity"]]:
                # Auto‑add missing DB field
                config["db_schema"][endpoint["entity"]].append({"name": field, "type": "string"})
    return config

def regenerate_layer(layer: str, context: dict) -> dict:
    # Call LLM again only for that layer, using context from other layers
    prompt = f"Re‑generate only the {layer} configuration. Existing context: {context}"
    return json.loads(call_llm(prompt))