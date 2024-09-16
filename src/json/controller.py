from fastapi import APIRouter

router = APIRouter()


@router.get("/api/json")
async def get_json_data(date: str):
    return {"message": f"Hello, {date}!"}