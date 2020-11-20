import os
import sys
import configparser


here = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    argv = [here, sys.argv[1]]
    print(f"Start Crawling With {argv[1]}")

    config_arg = argv[0] + '\\' + argv[1]

    config = configparser.ConfigParser()
    config.read(config_arg, None)
    is_crawl_company = bool(config['DEFAULT']['CrawlCompany'])
    is_crawl_people = bool(config['DEFAULT']['CrawlCompany'])
    is_crawl_people_related_company = bool(config['DEFAULT']['CrawlPeopleToCompany'])


    # TODO Main Crawling

    print(f"End Crawling With {argv[1]}")
