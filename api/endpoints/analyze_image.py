from repository_builders.ai_analysis_log_repository_builders import get_ai_analysis_log_repository
from repositories.ai_analysis_log_repository import AIAnalysisLogRepository
from services.analyze_image_service import AnalyzeImage
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from utils.date_util import get_jst_unix_timestamp

router = APIRouter()

# リクエストボディのモデル定義
class ImagePathRequest(BaseModel):
    image_path: str

# 分析結果を模擬的に返却するエンドポイント
@router.post("/")
async def analyze_image(request: ImagePathRequest,
    repository: AIAnalysisLogRepository = Depends(get_ai_analysis_log_repository)):
    start_time = get_jst_unix_timestamp()
    analyze_image = AnalyzeImage()
    image_description_response = analyze_image.analyze(request.image_path)
    end_time = get_jst_unix_timestamp()
    repository.create_ai_analysis_log(
        image_path=request.image_path,
        success=image_description_response.success,
        message=image_description_response.message,
        class_=image_description_response.estimated_data.get("class"),
        confidence=image_description_response.estimated_data.get("confidence"),
        request_timestamp=start_time,
        response_timestamp=end_time
    )
    
    return image_description_response