from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class People(Base):
    __tablename__ = "People"
    PeopleId = Column(Integer, primary_key=True, autoincrement=True)
    SearchedName = Column(String(800))
    NationalId = Column(String(100))
    FullName = Column(String(8000))
    Gender = Column(String(800))
    TagLine = Column(String(8000))
    Importance = Column(String(8000))
    CrawledDate = Column(DateTime)
