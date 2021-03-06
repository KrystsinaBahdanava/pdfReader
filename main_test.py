from configurator import Configurator
from connector import Connector
from sys import argv
from result import Result
from test_processor import TestProcessor


def run():
    config = Configurator(argv[1])
    database_url = config.get_database_url()
    connector = Connector(database_url)
    logger = Result()
    test_processor = TestProcessor(config, connector, logger)
    test_processor.process()

    logger.finish_test()


run()
