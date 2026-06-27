from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from sqlalchemy.orm import declarative_base

from datetime import datetime

from zoneinfo import ZoneInfo

Base = declarative_base()


class Job(Base):

    __tablename__ = "jobs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    company = Column(
        String,
        nullable=False
    )

    location = Column(
        String,
        nullable=False
    )

    link = Column(
        String,
        unique=True,
        nullable=False
    )

    description = Column(
        Text
    )

    scraped_at = Column(
    DateTime(timezone=True),
    default=lambda: datetime.now(
        ZoneInfo("Asia/Kolkata")
    )
)
