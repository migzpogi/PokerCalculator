from configparser import ConfigParser
import logging.config

log = logging.getLogger(__name__)

if __name__ == '__main__':
    # load config and initialize logging
    config = ConfigParser()
    config.read('./conf/settings.ini')

    logging.config.fileConfig(disable_existing_loggers=False,
                              fname='./logs/logging_config.ini',
                              defaults={'logfilename': config.get('logs', 'path')})

    log.info("hello world!")

