import jdatetime
from repository import search_pattern
import openpyxl
import pandas as pd


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


def load_pattern_from_file():
    patterns = search_pattern.patterns
    return patterns
