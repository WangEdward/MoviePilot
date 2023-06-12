from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import Session

from app.db.models import Base


class SiteIcon(Base):
    """
    站点图标表
    """
    id = Column(Integer, Sequence('id'), primary_key=True, index=True)
    name = Column(String, nullable=False)
    domain = Column(String, index=True)
    url = Column(String, nullable=False)
    base64 = Column(String)

    @staticmethod
    def get_by_domain(db: Session, domain: str):
        return db.query(SiteIcon).filter(SiteIcon.domain == domain).first()
