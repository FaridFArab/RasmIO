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

    def __init__(self, PeopleId=None, SearchedName=None, NationalId=None, FullName=None, Gender=None, TagLine=None, Importance=None, CrawledDate=None):
        self.PeopleId = PeopleId
        self.SearchedName = SearchedName
        self.NationalId = NationalId
        self.FullName = FullName
        self.Gender = Gender
        self.TagLine = TagLine
        self.Importance = Importance
        self.CrawledDate = CrawledDate