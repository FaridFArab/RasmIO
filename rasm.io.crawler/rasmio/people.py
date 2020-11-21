from rasmio.database import init_db

Base = init_db.Base
Column = init_db.Column
String = init_db.String
Integer = init_db.Integer
BigInteger = init_db.BigInteger
DateTime = init_db.DateTime
FK = init_db.ForeignKey


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

    def __init__(self, PeopleId, SearchedName, NationalId, FullName, Gender, TagLine, Importance, CrawledDate):
        self.PeopleId = PeopleId
        self.SearchedName = SearchedName
        self.NationalId = NationalId
        self.FullName = FullName
        self.Gender = Gender
        self.TagLine = TagLine
        self.Importance = Importance
        self.CrawledDate = CrawledDate

    @staticmethod
    def insert(obj_people):
        try:
            session = init_db.init_database()
            session.add(obj_people)
            session.commit()
            return True, str(0)
        except Exception as ex:
            print('error occured!', str(ex))
            return False, str(ex)
