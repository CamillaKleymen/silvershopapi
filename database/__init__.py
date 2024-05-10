from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLAlCHEMY_DATABASE_URL = 'sqlite:///data.db'
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:muxtar15ovchar@localhost/silvershopfastapi"

engine = create_engine(SQLAlCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

