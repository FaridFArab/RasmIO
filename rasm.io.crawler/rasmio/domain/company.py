from sqlalchemy import Column, Integer, String, DateTime
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

    def __init__(self, CompanyId=None, SearchedName=None, Id=None, Title=None, Status=None, RegistrationNo=None, RegistrationDate=None, Address=None,
                 PostalCode=None, EconomicalCode=None, Phone=None, EdareKol=None, VahedSabti=None, Description=None, Site=None, Fax=None, Email=None,
                 Latitude=None, Longitude=None, CrawledDate=None):
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