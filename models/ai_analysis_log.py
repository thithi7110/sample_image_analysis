from sqlalchemy import Column, Integer, String, DECIMAL, BigInteger
from models.database import Base

class AIAnalysisLog(Base):
    __tablename__ = "ai_analysis_log"
    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String(255))
    success = Column(String(255))
    message = Column(String(255))
    class_ = Column("class", Integer)
    confidence = Column(DECIMAL(5,4))
    request_timestamp = Column(BigInteger)
    response_timestamp = Column(BigInteger)
