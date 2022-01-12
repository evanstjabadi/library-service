from typing import Dict

class Controller():
    async def add_user(self, user: Dict):
        return await  {
        "status": "success",
        "data": user
    }

    async def get_root(self):
        return await  {
        "status": "success",
        "data": "Hello from user root"
    }
