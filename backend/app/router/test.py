from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def hello():
    """Hello world route to make sure the app is working correctly"""
    return {"msg": "Hello World From Fatin Shadab 🤓!"}