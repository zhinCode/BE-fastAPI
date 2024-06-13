import aiomysql
from .config import settings

class MySQLDatabaseProvider:
    def __init__(self):
        self.pool = None

    async def init_pool(self):
        try:
            self.pool = await aiomysql.create_pool(
                host=settings.database_host,
                port=int(settings.database_port),
                user=settings.database_user,
                password=settings.database_password,
                db=settings.database_name,
                minsize=1,
                maxsize=5,
            )
            print("Database pool initialized successfully.")
        except Exception as e:
            print(f"Error creating connection pool: {e}")
            self.pool = None

    async def query(self, query: str, params: tuple = None):
        if self.pool is None:
            await self.init_pool()
            if self.pool is None:
                raise ConnectionError("Database pool is not initialized.")
        async with self.pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(query, params)
                result = await cursor.fetchall()
                return result

database = MySQLDatabaseProvider()
