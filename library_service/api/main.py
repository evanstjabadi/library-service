from fastapi import FastAPI

from library_service.api.routers import users

def create_app()->FastAPI:
    app = FastAPI()
    app.debug = True
    app.include_router(users.router)

    return app

app = create_app()

app.include_router(users.router)
