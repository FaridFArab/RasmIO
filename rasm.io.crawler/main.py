import os
import sys
from rasmio.config_parser import parse_config_ini


here = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    print(f"Start reading config...")
    argv = [here, sys.argv[1]]
    config_arg = argv[0] + '\\' + argv[1]
    print(f"End reading config...")
    config_dict = parse_config_ini(config_arg)
    print(f"Start crawling with {argv[1]} mode")



    # TODO Main Crawling

    print(f"End crawling with {argv[1]}")
