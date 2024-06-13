from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import HTTPException as FastAPIHTTPException
from app.services.common.schemas import *

class ResponseHandler:
    @staticmethod
    def handle_response(error: Exception, result: any = None):
        if error:
            if isinstance(error, RequestValidationError):
                response = ValidationErrorResponse(
                    status="reject",
                    reason={"detail": [ValidationErrorDetail(loc=e["loc"], msg=e["msg"], type=e["type"]) for e in error.errors()]}
                )
                return JSONResponse(status_code=422, content=response.model_dump())
            elif isinstance(error, FastAPIHTTPException) or isinstance(error, StarletteHTTPException):
                response = ErrorResponse(status="error", error={"code": str(error.status_code), "message": error.detail})
                return JSONResponse(status_code=error.status_code, content=response.model_dump())
            else:
                response = ErrorResponse(status="error", error={"code": "500", "message": str(error)})
                return JSONResponse(status_code=500, content=response.model_dump())
        response = SuccessResponse(status="success", data=result)
        return JSONResponse(status_code=200, content=response.model_dump())
    
    @staticmethod
    def get_responses():
        return {
            500: {"model": ErrorResponse},
            422: {"model": ValidationErrorResponse}
        }

def resp():
    return {"response_model": SuccessResponse, "responses": ResponseHandler.get_responses()}
