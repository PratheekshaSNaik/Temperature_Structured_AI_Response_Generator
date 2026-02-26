from pydantic import BaseModel
from typing import List

class StructuredResponse(BaseModel):
    summary: str
    key_points: List[str]
    conclusion: str