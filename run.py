'''Running the Xetra ETL application'''
import logging
import logging.config

import yaml

def main():
    '''
    entry point to run xetra ETL job
    '''
    #parse YAML file
    config_path = 'C:/Users/GGPC/Desktop/Python/ETL Pipelines/xetra_project/xetra_1234/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger  = logging.getLogger(__name__)
    logger.info('this is a test.')


if __name__ == '__main__':
    main()