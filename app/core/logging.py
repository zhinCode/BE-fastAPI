import time
from datetime import datetime
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import logging

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = (time.time() - start_time) * 1000  # milliseconds
        formatted_process_time = f"{process_time:.2f} ms"
        
        timestamp = datetime.now().astimezone().isoformat()
        log_message = f"{timestamp} - {request.method} {request.url.path} - {response.status_code} - {formatted_process_time}"
        
        logging.info(log_message)
        return response
