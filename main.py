from dotenv import load_dotenv
load_dotenv()
from repository_builders.ai_analysis_log_repository import get_ai_analysis_log_repository
from repositories.ai_analysis_log_repository import AIAnalysisLogRepository
from services.analyze_image_service import AnalyzeImage
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# リクエストボディのモデル定義
class ImagePathRequest(BaseModel):
    image_path: str

# 分析結果を模擬的に返却するエンドポイント
@app.post("/analyze-image/")
async def analyze_image(request: ImagePathRequest,
    repository: AIAnalysisLogRepository = Depends(get_ai_analysis_log_repository)):
    analyze_image = AnalyzeImage()
    image_description_response = analyze_image.analyze(request.image_path)
    repository.create_ai_analysis_log(
        image_path=request.image_path,
        success=image_description_response.success,
        message=image_description_response.message,
        class_=image_description_response.estimated_data.get("class"),
        confidence=image_description_response.estimated_data.get("confidence"),
        request_timestamp=0,
        response_timestamp=0
    )
    
    return image_description_response