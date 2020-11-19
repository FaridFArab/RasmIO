import jdatetime
from rasmio.repository import search_pattern
import pandas as pd
from pandas import ExcelWriter
from rasmio import people, company
from datetime import datetime


def convert_gregorian_date_to_jalali_date(gregorian_datetime):
    gregorian_date = gregorian_datetime.rsplit('T', 1)[0]
    parsed_gregorian_date = gregorian_date.split('-')
    jalili_date = str(jdatetime.date.fromgregorian(day=int(parsed_gregorian_date[2]), month=int(parsed_gregorian_date[1]), year=int(parsed_gregorian_date[0])))
    jalili_date = jalili_date.replace('-', '/')
    return jalili_date


def load_pattern_from_excel():
    df = pd.ExcelFile('repository/suppliers.xlsx').parse('Sheet1')
    suppliers = []
    for supplier in df.Name:
        suppliers.append(supplier)
    return suppliers


def load_people_pattern_from_excel():
    df = pd.ExcelFile('repository/people.xlsx').parse('Sheet1')
    suppliers = []
    for supplier in df.Name:
        suppliers.append(supplier)
    return suppliers


def load_pattern_from_excel_split():
    df = pd.ExcelFile('repository/suppliers.xlsx').parse('Sheet1')
    suppliers = []
    for supplier in df.Name:
        splited_suppliers = supplier.split(' ')
        for sup in splited_suppliers:
            suppliers.append(sup)
    return suppliers


def load_pattern_from_file():
    patterns = search_pattern.pattern_2
    return patterns


def write_to_excel(supplier_df):
    writer = ExcelWriter('Suppliers.xlsx')
    supplier_df.to_excel(writer, 'Sheet1')
    writer.save()


def add_company_to_db(dict_company: dict) -> bool:
    obj_company = company.Company(CompanyId=None, SearchedName=dict_company['searched_name'], Id=str(dict_company['id']), Title=dict_company['title'],
                                  Status=dict_company['status'],
                                  RegistrationNo=str(dict_company['registration_no']), RegistrationDate=str(dict_company['registration_date']),
                                  Address=dict_company['address'],
                                  PostalCode=str(dict_company['postal_code']), EconomicalCode=str(dict_company['economical_code']), Phone=str(dict_company['phone']),
                                  EdareKol=dict_company['edare_kol'],
                                  VahedSabti=dict_company['vahed_sabti'], Description=dict_company['description'], Site=dict_company['site'],
                                  Fax=str(dict_company['fax']),
                                  Email=dict_company['email'], Latitude=str(dict_company['latitude']), Longitude=str(dict_company['longitude']), CrawledDate=datetime.now())
    status, result = company.Company.insert(obj_company)
    return status


def add_people_to_db(dict_people: dict) -> bool:
    obj_people = people.People(PeopleId=None, SearchedName=str(dict_people['searched_name']), FullName=str(dict_people['full_name']),
                               NationalId=str(dict_people['national_id']), Gender=str(dict_people['gender']), TagLine=str(dict_people['tag_line']),
                               Importance=str(dict_people['importance']), CrawledDate=datetime.now())
    status, result = people.People.insert(obj_people)
    return status

