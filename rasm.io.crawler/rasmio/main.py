import logging

logging.basicConfig(filename='logs/suppliers.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


def start_crawling(config_dict):
    if config_dict['is_crawl_company']:
        pass
        # TODO Crawl Company (https://rasm.io/api/newsearch?term=<SearchTerm>&entity=company&page=1&pagesize=50)
    if config_dict['is_crawl_people']:
        pass
        # TODO Crawl People (https://rasm.io/api/newsearch?term=<SearchTerm>&entity=person&page=1&pagesize=5)

