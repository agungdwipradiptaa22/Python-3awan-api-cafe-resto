from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.dialects import registry

# Register psycopg v3 as default PostgreSQL driver
registry.register("postgresql", "sqlalchemy.dialects.postgresql.psycopg", "PGDialect_psycopg")

# Gunakan psycopg v3
DATABASE_URL = "postgresql://postgres:ORnTWzLkAfHzZCAtVHPbHHLbXccAFMnK@shinkansen.proxy.rlwy.net:40405/railway"

# Buat engine
engine = create_engine(DATABASE_URL, echo=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base untuk model ORM
Base = declarative_base()

# Dependency generator untuk mendapatkan session di tiap request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
