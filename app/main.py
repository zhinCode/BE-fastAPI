from fastapi import FastAPI
from app.core.error_handler import add_exception_handlers
from app.services.common.routes import router as common_router
from app.services.users.routes import router as users_router
from app.core.config import settings
from app.core.logging import LoggingMiddleware
import uvicorn
import logging
from app.logo import display_logo, display_app_info


logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.add_middleware(LoggingMiddleware)

add_exception_handlers(app)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(common_router, prefix="/api")
app.include_router(users_router, prefix="/api")

if __name__ == "__main__":
    display_logo()
    display_app_info(settings.app_version, settings.app_author)
    uvicorn.run(app, host="0.0.0.0", port=settings.app_port, access_log=False)
