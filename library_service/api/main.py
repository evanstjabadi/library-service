from fastapi import FastAPI

from library_service.api.routers import books, users


def create_app() -> FastAPI:
    app = FastAPI()
    app.debug = True

    return app


app = create_app()

app.include_router(users.router)
app.include_router(books.router)


@app.get("/")
async def root():
    return {"message": "Hello and welcome to the library!"}
