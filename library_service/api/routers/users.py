from typing import Dict

from fastapi import APIRouter

from library_service.controllers.users import Controller

controller = Controller()


router = APIRouter()

router.get("/users")
async def user_root():
    result = controller.get_root()
    return {
        "status": "success",
        "data": "Hello from user root",
        "controller_data": result
    }


router.post("/users")
async def add_user(user: Dict):
    try:
        result = await controller.add_user(user)
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
    }
