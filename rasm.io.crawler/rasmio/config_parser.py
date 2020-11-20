from configparser import ConfigParser


def parse_config_ini(config_arg) -> dict:
    config = ConfigParser()
    config.read(config_arg, None)

    config_dict = {
        'is_crawl_company': bool(config['DEFAULT']['CrawlCompany']),
        'is_crawl_people': bool(config['DEFAULT']['CrawlPeople']),
        'is_crawl_people_related_company': bool(config['DEFAULT']['CrawlPeopleToCompany']),
        'crawling_sleep_time': str(config['DEFAULT']['CrawlerSleepTime']),
        'write_to_database': bool(config['DEFAULT']['WriteToDatabase']),
        'write_to_excel': bool(config['DEFAULT']['WriteToExcelFile']),
        'database_connection_string': str(config['DataBase']['RasmioURL']),
    }

    return config_dict
