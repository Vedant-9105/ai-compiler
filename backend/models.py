from pydantic import BaseModel, Field, validator
from typing import List, Dict, Optional

class EntityField(BaseModel):
    name: str
    type: str  # string, int, bool, date, reference
    required: bool = True
    reference_to: Optional[str] = None

class Entity(BaseModel):
    name: str
    fields: List[EntityField]

class APIEndpoint(BaseModel):
    path: str
    method: str  # GET, POST, PUT, DELETE
    entity: str
    fields: List[str]  # fields returned/accepted
    roles_allowed: List[str]

class UIPage(BaseModel):
    name: str
    route: str
    components: List[Dict]  # {"type": "form", "entity": "contact"}

class AuthRule(BaseModel):
    role: str
    resource: str
    actions: List[str]  # create, read, update, delete

class FinalConfig(BaseModel):
    db_schema: Dict[str, List[EntityField]]
    api_config: List[APIEndpoint]
    ui_config: List[UIPage]
    auth_config: List[AuthRule]
    metadata: Dict = {}  # for assumptions, warnings