from fastapi import APIRouter
from app.controller.juscaba import JuscabaController

router = APIRouter()


@router.get("/details/{identificador}")
def get_details(identificador: str):
    return JuscabaController.get_first(identificador)
