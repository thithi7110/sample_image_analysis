
from fastapi import APIRouter
from api.endpoints import (
    analyze_image,
)
router = APIRouter()
@router.get("/")
async def root(message: str):
    return {"message": message}

#APIルーターの設定(下記エンドポイントを追加していく)
router.include_router(analyze_image.router, prefix="/analyze-image", tags=["画像分析"])