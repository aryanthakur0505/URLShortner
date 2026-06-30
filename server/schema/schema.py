"""
The schema can be considered as a blueprint or guideline for the structure of the documents.
It typically defines the fields present in the documents, their data types, and any validation rules
"""

from pydantic import BaseModel
from typing import Optional

class UrlMappingSchema(BaseModel):
    short_url: Optional[str] = None
    long_url: str
