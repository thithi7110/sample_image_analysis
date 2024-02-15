from contextlib import contextmanager
from sqlalchemy.ext.asyncio import AsyncSession

class BaseRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    @contextmanager
    def session_scope(self):
        """セッションのスコープを管理するコンテキストマネージャー"""
        session = self.db_session
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
