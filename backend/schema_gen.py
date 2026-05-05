SCHEMA_PROMPT = """
Convert the system design into concrete schemas:

1. DB schema (SQL DDL as JSON): 
   {"table_name": [{"name":"id","type":"int","required":true}]}
2. API config (OpenAPI-style):
   {"paths": {...}, "components": {...}}
3. UI config (JSON components per page)
4. Auth config (role → permissions list)

System design: {design}
"""

def generate_schemas(design: dict) -> dict:
    prompt = SCHEMA_PROMPT.format(design=json.dumps(design))
    raw = call_llm(prompt)
    return json.loads(raw)