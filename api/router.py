from fastapi import APIRouter

from api.routes import books
from api.routes import tests

api_router = APIRouter()

api_router.include_router(books.router, prefix="/books", tags=["books"])
api_router.include_router(tests.router, tags=["tests"]) 
