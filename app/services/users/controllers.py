from app.core.database import database
from app.services.users.schemas import User, UserCreate, UserUpdate

async def create_user(user_data: UserCreate):
    error = None
    result = None
    try:
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        params = (user_data.name, user_data.email)
        await database.query(query, params)
        result = {"message": "User created successfully"}
    except Exception as e:
        error = e
    return error, result

async def read_users():
    error = None
    result = None
    try:
        result = await database.query("SELECT id, name, email FROM users")
        result = [User(id=row["id"], name=row["name"], email=row["email"]) for row in result]
    except Exception as e:
        error = e
    return error, result

async def update_user(user_id: int, user_data: UserUpdate):
    error = None
    result = None
    try:
        query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
        params = (user_data.name, user_data.email, user_id)
        await database.query(query, params)
        result = {"message": "User updated successfully"}
    except Exception as e:
        error = e
    return error, result

async def delete_user(user_id: int):
    error = None
    result = None
    try:
        query = "DELETE FROM users WHERE id = %s"
        params = (user_id,)
        await database.query(query, params)
        result = {"message": "User deleted successfully"}
    except Exception as e:
        error = e
    return error, result
