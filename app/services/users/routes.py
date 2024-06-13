from fastapi import APIRouter
from app.services.users.controllers import *
from app.services.users.schemas import *
from app.core.response_handler import ResponseHandler, resp

router = APIRouter()

@router.get("/users", **resp())
async def get_users():
    error, result = None, None
    try:
        error, result = await read_users()
    except Exception as e:
        error = e
    finally:
        return ResponseHandler.handle_response(error, result)

@router.post("/users", **resp())
async def add_user(user: UserCreate):
    error, result = None, None
    try:
        error, result = await create_user(user)
    except Exception as e:
        error = e
    finally:
        return ResponseHandler.handle_response(error, result)

@router.put("/users/{user_id}", **resp())
async def modify_user(user_id: int, user: UserUpdate):
    error, result = None, None
    try:
        error, result = await update_user(user_id, user)
    except Exception as e:
        error = e
    finally:
        return ResponseHandler.handle_response(error, result)

@router.delete("/users/{user_id}", **resp())
async def remove_user(user_id: int):
    error, result = None, None
    try:
        error, result = await delete_user(user_id)
    except Exception as e:
        error = e
    finally:
        return ResponseHandler.handle_response(error, result)
