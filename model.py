from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')

class Diaper(BaseModel):
    id: str = None
    title: str
    description: str
    color: str
    size: str


class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None