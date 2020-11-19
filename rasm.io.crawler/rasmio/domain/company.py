from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Sequence, Integer, String, create_engine, BigInteger, DateTime, Float, DECIMAL, Date, ForeignKey, or_, desc
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Company(Base):
    __tablename__ = "Company"
    CompanyId = Column(Integer, primary_key=True, autoincrement=True)
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