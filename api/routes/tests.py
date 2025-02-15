from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


router = APIRouter()

@router.get("/testcd", status_code=status.HTTP_200_OK)
async def testcd():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"testcd": "passed"})