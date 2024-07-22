from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_session():
    db_url = "postgresql://postgres:123456@localhost:5432/iot"
    engine = create_engine(db_url)

    session = sessionmaker(bind=engine)
    return session()
