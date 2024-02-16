from dotenv import load_dotenv
load_dotenv()
from repository_builders.ai_analysis_log_repository_builders import get_ai_analysis_log_repository
from repositories.ai_analysis_log_repository import AIAnalysisLogRepository
from services.analyze_image_service import AnalyzeImage
from fastapi import APIRouter, Depends, FastAPI, HTTPException
from pydantic import BaseModel
from api.api import router as api_router
from fastapi.logger import logger

app = FastAPI(
    title="sample_image_analyzer",
    openapi_url=f"/openapi.json",
    description="This is a sample image analyzer API.",
)

try:
    app.include_router(api_router, prefix="/api", tags=["API"])

except AttributeError as e:
    logger.error(f"exception: {e}")
except Exception as e:
    logger.error(f"exception: {e}")