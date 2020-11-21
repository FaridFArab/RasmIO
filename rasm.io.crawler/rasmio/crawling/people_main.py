from rasmio import utility
import requests
import logging

logging.basicConfig(filename='people.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

peoples = utility.load_people_pattern_from_excel()
counter = 0
retrieved_data = []
for people in peoples:
    str_people = str(people)
    print("Crawling data for name: ", str_people)
    main_url = 'https://rasm.io/api/search'
    get_parameters = {'term': str_people, 'page': '1',
                      'pagesize': 10000}  # pagesize: for number of retrieved records,  page: number of page, term: specific url
    try:
        result = requests.get(url=main_url, params=get_parameters, )
        raw_data = result.json()
        data = result.json()['people']['hits']['hits']
        for row in data:
            people_data = row['_source']
            dict_people_info = {}

            national_id = people_data.get('id', '0')
            full_name = people_data.get('title', '0')
            gender = people_data.get('gender', '0')  # True: Male , False: Female
            tag_line = people_data.get('tagline', '0')
            importance = people_data.get('importance', '0')

            dict_people_info['searched_name'] = str(str_people)
            dict_people_info['national_id'] = national_id
            dict_people_info['full_name'] = full_name
            dict_people_info['gender'] = gender
            dict_people_info['tag_line'] = tag_line
            dict_people_info['importance'] = importance
            retrieved_data.append(dict_people_info)
            result_status = utility.add_people_to_db(dict_people_info)
            counter = counter + 1
    except Exception as ex:
        logging.error('Error in crawling ' + str_people + ' with this error: ' + str(ex))
        continue
