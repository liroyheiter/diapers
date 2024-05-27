import motor.motor_asyncio

MONGODB_URL = f"mongodb+srv://vhan228337:228337@liroy.ou9f8vh.mongodb.net/?retryWrites=true&w=majority&appName=Liroy"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = client.python_bd