from fastapi import Depends
from models.database import SessionLocal, get_db
from repositories.ai_analysis_log_repository import AIAnalysisLogRepository


def get_ai_analysis_log_repository(db = Depends(get_db)):
    return AIAnalysisLogRepository(db)