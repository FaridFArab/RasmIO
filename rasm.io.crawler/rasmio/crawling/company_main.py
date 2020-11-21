from rasmio.utility.utility import load_pattern_from_excel, log_file, convert_gregorian_date_to_jalali_date, log_error
import requests



def crawl_company():
    log_file()
    companies = load_pattern_from_excel()  # load data from input excel

    counter = 0
    retrieved_data = []
    for company in companies:
        str_company = str(company)
        print(f"Crawling data for company name: {str_company}")
        main_url = 'https://rasm.io/api/search'
        get_parameters = {'term': str_company, 'page': '1',
                          'pagesize': 50}  # pagesize: for number of retrieved records,  page: number of page, term: specific url
        try:
            result = requests.get(url=main_url, params=get_parameters, )
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
                edare_kol = company_data.get('edareKol', '0')
                vahed_sabti = company_data.get('vahedSabti', '0')
                description = company_data.get('description', '0')
                site = company_data.get('site', '0')
                fax = company_data.get('fax', '0')
                email = company_data.get('email', '0')
                latitude = company_data.get('lat', '0')
                longitude = company_data.get('lng', '0')

                dict_company_info['searched_name'] = str(company)
                dict_company_info['id'] = id
                dict_company_info['title'] = title
                dict_company_info['status'] = status
                dict_company_info['registration_no'] = registration_no
                dict_company_info['registration_date'] = jalali_registration_date
                dict_company_info['address'] = address
                dict_company_info['postal_code'] = postal_code
                dict_company_info['economical_code'] = economical_code
                dict_company_info['phone'] = phone
                dict_company_info['edare_kol'] = edare_kol
                dict_company_info['vahed_sabti'] = vahed_sabti
                dict_company_info['description'] = description
                dict_company_info['site'] = site
                dict_company_info['fax'] = fax
                dict_company_info['email'] = email
                dict_company_info['latitude'] = latitude
                dict_company_info['longitude'] = longitude

                # result_status = add_company_to_db(dict_company_info)
                retrieved_data.append(dict_company_info)
                counter = counter + 1
                print(str(title))
        except Exception as ex:
            print('Error: ' + str(ex))
            log_error(str_company, ex)
                # if counter % 1000 == 500:
                #     print(counter)
                #     print("Sleeping...")
                #     time.sleep(8)
        # supplier_df = pd.DataFrame(retrieved_data)
        # utility.write_to_excel(supplier_df)
