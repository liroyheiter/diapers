from fastapi import APIRouter
from repository import DiaperRepo
from model import Diaper, Response

router = APIRouter()


@router.get("/diaper/")
async def get_all_diaper():
    _diaperList = await DiaperRepo.retrieve()
    return Response(code=200, status="OK", message="All diapers retrieved lol", result=_diaperList).dict(exclude_none=True)

@router.post("/diaper/create")
async def create(diaper: Diaper):
    await DiaperRepo.insert(diaper)
    return Response(code=200, status="OK", message="Diaper created lol").dict(exclude_none=True)

@router.get("/diaper/{id}")
async def get_id(id:str):
    _diaper = await DiaperRepo.retrieve_id(id)
    return Response(code=200, status="OK", message="Diaper retrieved lol", result=_diaper).dict(exclude_none=True)

@router.post("/diaper/update")
async def update(diaper: Diaper):
    await DiaperRepo.update(diaper)
    return Response(code=200, status="OK", message="Diaper updated lol").dict(exclude_none=True)

@router.delete("/diaper/{id}")
async def delete(id:str):
    await DiaperRepo.delete(id)
    return Response(code=200, status="OK", message="Diaper deleted lol").dict(exclude_none=True)