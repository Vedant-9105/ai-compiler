DESIGN_PROMPT = """
Based on the following intent, produce a system design as JSON:
{
  "entities": [{"name": "...", "fields": [{"name":"...","type":"string"}]}],
  "relations": [{"from":"EntityA","to":"EntityB","type":"one-to-many"}],
  "api_endpoints": [{"path":"/api/...","method":"GET","entity":"...","roles_allowed":["admin"]}],
  "ui_pages": [{"name":"Dashboard","route":"/dashboard","components":[...]}],
  "business_rules": ["Premium users can access analytics"]
}

Intent: {intent}
"""

def design_system(intent: dict) -> dict:
    prompt = DESIGN_PROMPT.format(intent=json.dumps(intent))
    return json.loads(call_llm(prompt))