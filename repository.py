from model import Diaper
from config import database
import uuid

class DiaperRepo():
    @staticmethod
    async def retrieve():
        _diaper = []
        collection = database.get_collection('diaper').find()
        async for diaper in collection:
            _diaper.append(diaper)
        return _diaper
    
    @staticmethod
    async def insert(diaper: Diaper):
        id = str(uuid.uuid4())
        _diaper = {
            "_id": id,
            "title": diaper.title,
            "description": diaper.description,
            "color": diaper.color,
            "size": diaper.size
        }
        await database.get_collection('diaper').insert_one(_diaper)  # Insert _diaper instead of diaper

    @staticmethod
    async def update(id:str, diaper: Diaper):
        _diaper = await database.get_collection('diaper').find_one({"_id":id})
        _diaper["title"] = diaper.title
        _diaper["description"] = diaper.description
        _diaper["color"] = diaper.color
        _diaper["size"] = diaper.size
        await database.get_collection('diaper').update_one({"_id":id}, {"$set":_diaper})

    @staticmethod
    async def retrieve_id(id:str):
        await database.get_collection('diaper').find_one({"_id":id})

    @staticmethod
    async def delete(id:str):  # Corrected method name
        await database.get_collection('diaper').delete_one({"_id":id})
