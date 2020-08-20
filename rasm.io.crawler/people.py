import init_db

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
    Id = Column(String(800))
    Title = Column(String(800))
    Status = Column(String(800))
    RegistrationNo = Column(String(800))
    RegistrationDate = Column(String(800))
    Address = Column(String(800))
    PostalCode = Column(String(800))
    EconomicalCode = Column(String(800))
    Phone = Column(String(800))
    EdareKol = Column(String(800))
    VahedSabti = Column(String(800))
    Description = Column(String(800))
    Site = Column(String(800))
    Fax = Column(String(800))
    Email = Column(String(800))
    Latitude = Column(String(800))
    Longitude = Column(String(800))
    CrawledDate = Column(DateTime)

    def __init__(self, CompanyId, SearchedName, Id, Title, Status, RegistrationNo, RegistrationDate, Address, PostalCode, EconomicalCode, Phone, EdareKol,
                 VahedSabti, Description, Site, Fax, Email, Latitude, Longitude, CrawledDate):
        self.CompanyId = CompanyId
        self.SearchedName = SearchedName
        self.Id = Id
        self.Title = Title
        self.Status = Status
        self.RegistrationNo = RegistrationNo
        self.RegistrationDate = RegistrationDate
        self.Address = Address
        self.PostalCode = PostalCode
        self.EconomicalCode = EconomicalCode
        self.Phone = Phone
        self.EdareKol = EdareKol
        self.VahedSabti = VahedSabti
        self.Description = Description
        self.Site = Site
        self.Fax = Fax
        self.Email = Email
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.CrawledDate = CrawledDate

    @staticmethod
    def insert(obj_company):
        try:
            session = init_db.init_database()
            x = obj_company
            session.add(obj_company)
            session.commit()
            return True, str(0)
        except Exception as ex:
            print('error occured!', str(ex))
            return False, str(ex)
