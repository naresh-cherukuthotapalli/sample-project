
from pydantic import BaseModel
from typing import List, Dict
from typing import Union, List

class ToolStep(BaseModel):
    tool: str
    input: Dict[str, str]

class Workflow(BaseModel):
    name: str
    steps: List[ToolStep]
