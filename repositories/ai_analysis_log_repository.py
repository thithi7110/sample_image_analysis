from sqlalchemy.future import select
from sqlalchemy import update, delete
from models.ai_analysis_log import AIAnalysisLog
from repositories.base_repository import BaseRepository


class AIAnalysisLogRepository(BaseRepository):
    def get_ai_analysis_log(self, log_id: int):
        with self.session_scope() as session:
            result = session.execute(select(AIAnalysisLog).filter(AIAnalysisLog.id == log_id))
            return result.scalars().first()

    def get_ai_analysis_logs(self, offset, limit):
        with self.session_scope() as session:
            result = session.execute(
                select(AIAnalysisLog).offset(offset).limit(limit)
            )
            return result.scalars().all()

    def create_ai_analysis_log(
        self, 
        image_path,
        success,
        message,
        class_,
        confidence,
        request_timestamp,
        response_timestamp):
        with self.session_scope() as session:
            ai_analysis_log = AIAnalysisLog(
                image_path=image_path,
                success=success,
                message=message,
                class_=class_,
                confidence=confidence,
                request_timestamp=request_timestamp,
                response_timestamp=response_timestamp
            )
            session.add(ai_analysis_log)