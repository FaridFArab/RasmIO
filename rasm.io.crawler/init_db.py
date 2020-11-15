from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Sequence, Integer, String, create_engine, BigInteger, DateTime, Float, DECIMAL, Date, ForeignKey, or_, desc
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def init_database():
    db_url = 'mssql+pyodbc://sa:10484617@localhost/Rasmio?driver=SQL Server Native Client 11.0'
    engine = create_engine(db_url)
    session = sessionmaker(bind=engine)
    session = session()
    return session
