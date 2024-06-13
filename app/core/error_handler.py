from fastapi import Request, HTTPException as FastAPIHTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.response_handler import ResponseHandler

async def unified_exception_handler(request: Request, exc: Exception):
    return ResponseHandler.handle_response(exc)

def add_exception_handlers(app):
    app.add_exception_handler(RequestValidationError, unified_exception_handler)
    app.add_exception_handler(FastAPIHTTPException, unified_exception_handler)
    app.add_exception_handler(StarletteHTTPException, unified_exception_handler)
    app.add_exception_handler(Exception, unified_exception_handler)
