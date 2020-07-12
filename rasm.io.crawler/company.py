import init_db

Base = init_db.Base
Column = init_db.Column
String = init_db.String
Integer = init_db.Integer
BigInteger = init_db.BigInteger
DateTime = init_db.DateTime
FK = init_db.ForeignKey


class Company(Base):
    __tablename__ = "Company"
    CompanyId = Column(Integer, primary_key=True, autoincrement=True)
    SearchedName = Column(String(256))
    Id = Column(String(256))
    Title = Column(String(256))
    Status = Column(String(256))
    RegistrationNo = Column(String(256))
    RegistrationDate = Column(String(256))
    Address = Column(String(256))
    PostalCode = Column(String(256))
    EconomicalCode = Column(String(256))
    Phone = Column(String(256))
    EdareKol = Column(String(256))
    VahedSabti = Column(String(256))
    Description = Column(String(256))
    Site = Column(String(256))
    Fax = Column(String(256))
    Email = Column(String(256))
    Latitude = Column(String(256))
    Longitude = Column(String(256))
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
