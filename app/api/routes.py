from fastapi import APIRouter, Query
from app.services.fizzbuzz import generate_fizzbuzz
from app.core.logging_config import logger

router = APIRouter()


@router.get("/fizzbuzz")
def fizzbuzz(
    int1: int = Query(gt=0),
    int2: int = Query(gt=0),
    limit: int = Query(gt=0),
    str1: str = Query(...),
    str2: str = Query(...)
):

    logger.info(f"Request received: int1={int1}, int2={int2}, limit={limit}")

    result = generate_fizzbuzz(int1, int2, limit, str1, str2)

    return {"result": result}