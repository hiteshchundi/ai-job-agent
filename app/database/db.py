from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    "postgresql://postgres:youneverknow@localhost/ai_job_agent"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)