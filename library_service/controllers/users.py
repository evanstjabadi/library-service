from typing import Dict

class Controller():
    def add_user(self, user: Dict):
        return  {
        "status": "success",
        "data": user
    }

    def get_root(self):
        return { 
            "status": "success",
            "data": "Hello from user root controller"
        }
