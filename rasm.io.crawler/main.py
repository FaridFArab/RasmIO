from repository import search_pattern
import pandas as pd
import requests
import time
import jdatetime
from pandas import ExcelWriter
import openpyxl


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


suppliers = load_pattern_from_excel()
# suppliers = load_pattern_from_file()
counter = 0
retrieved_data = []
for supplier in suppliers:
    str_supplier = str(supplier)
    print("Crawling data for company name: ", str_supplier)
    main_url = 'https://rasm.io/api/search'
    get_parameters = {'term': str_supplier, 'page': '1', 'pagesize': 10000}  # pagesize: for number of retrieved records,  page: number of page, term: specific url
    result = requests.get(url=main_url, params=get_parameters)
    raw_data = result.json()
    data = result.json()['companies']['hits']['hits']
    for row in data:
        company_data = row['_source']
        dict_company_info = {}
        id = company_data.get('id', '0')
        title = company_data.get('title', '0')
        status = company_data.get('status', '0')
        registration_no = company_data.get('registrationNo', '0')
        registration_date = company_data.get('registrationDate', '0')
        jalali_registration_date = '0'
        try:
            if registration_date != '0':
                jalali_registration_date = convert_gregorian_date_to_jalali_date(registration_date)
            else:
                jalali_registration_date = '0'
        except:
            jalali_registration_date = '0'
        address = company_data.get('address', '0')
        postal_code = company_data.get('postalCode', '0')
        economical_code = company_data.get('taxNumber', '0')
        phone = company_data.get('tel', '0')

        dict_company_info['searched_name'] = str(supplier)
        dict_company_info['id'] = id
        dict_company_info['title'] = title
        dict_company_info['status'] = status
        dict_company_info['registration_no'] = registration_no
        dict_company_info['registration_date'] = jalali_registration_date
        dict_company_info['address'] = address
        dict_company_info['postal_code'] = postal_code
        dict_company_info['economical_code'] = economical_code
        dict_company_info['phone'] = phone
        retrieved_data.append(dict_company_info)
        counter = counter + 1
        # print(counter)
        if str(counter) in ('100', '300', '500', '800', '1100', '1400', '1800', '2200', '2800', '3300', '3900', '4200', '4800', '4900'):
            print(counter)
            print("Sleeping...")
            time.sleep(15)
        # print(dict_company_info)
    # time.sleep(2)
supplier_df = pd.DataFrame(retrieved_data)
writer = ExcelWriter('CrawledSupplier.xlsx')
supplier_df.to_excel(writer, 'Sheet1')
writer.save()
