from flask import Flask, render_template,request
import jdatetime
import requests
import json


app = Flask(__name__)


def convert_gregorian_date_to_jalali_date(gregorian_datetime):
    gregorian_date = gregorian_datetime.rsplit('T', 1)[0]
    parsed_gregorian_date = gregorian_date.split('-')
    jalili_date = str(jdatetime.date.fromgregorian(day=int(parsed_gregorian_date[2]), month=int(parsed_gregorian_date[1]), year=int(parsed_gregorian_date[0])))
    jalili_date = jalili_date.replace('-', '/')
    return jalili_date


def crawl_rasmio(supplier_name, count):
    main_url = 'https://rasm.io/api/search'
    get_parameters = {'term': supplier_name, 'page': '1', 'pagesize': count}  # pagesize: for number of retrieved records,  page: number of page, term: specific url
    result = requests.get(url=main_url, params=get_parameters)
    data = result.json()['companies']['hits']['hits']
    retrieved_data = []
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

        dict_company_info['searched_name'] = str(supplier_name)
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
    return retrieved_data


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/rasmio', methods=['POST'])
def rasmio_crawler():
    data = request.get_json()
    name = data['name']
    count = data['count']
    result = crawl_rasmio(name, count)
    value = {"Results": result}
    return value


if __name__ == '__main__':
    app.run()
