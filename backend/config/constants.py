import configparser
import os


class Constants:
    # Path to the configuration file
    # Change this path to the relevant file location if needed
    _config_file = "/Volumes/arun/TTM_Project/ttm/backend/config/config.ini"
    
    @classmethod
    def _get_config(cls):
        config = configparser.ConfigParser()
        config.read(cls._config_file)
        return config

    @classmethod
    def get_working_capital_file(cls):
        config = cls._get_config()
        return config['Paths']['WorkingCapitalData']

    @classmethod
    def get_pnl_file(cls):
        config = cls._get_config()
        return config['Paths']['PNLData']
        