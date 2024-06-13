from pydantic import BaseModel
from typing import List, Any, Dict

class SuccessResponse(BaseModel):
    status: str = "success"
    data: Any

class ErrorResponse(BaseModel):
    status: str = "error"
    error: Dict[str, str]

class ValidationErrorDetail(BaseModel):
    loc: List[Any]
    msg: str
    type: str

class ValidationErrorResponse(BaseModel):
    status: str = "reject"
    reason: Dict[str, List[ValidationErrorDetail]]
