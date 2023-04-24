from Preprocessing_Module_Binary_Classifier import *
from Preprocessing_Module_Continuous_Classifier import *
from LocalLogicModule import *
from tkinter import filedialog
import configparser
from tkinter import *


class API_Controller:
    def __init__(self):
        config = Config()
    def buildBinaryModelVaporRoomAir(self):
        cfg = Config()
        print("Select the directory that contains the plexon files that you want to train the model on")
        sample_data = filedialog.askdirectory()
        access_obj = AccessData(sample_data, cfg)
    def buildContinuousModelConsumption(self):
        cfg = Config
        print("Select the directory that contains the plexon files that you want to train the model on")
        sample_data = filedialog.askdirectory()
        access_obj = AccessData(sample_data, cfg)
        return 0

    def create_continuous_config_file(self):
        config = configparser.ConfigParser()
        cfg = Config()

        config["DEFAULT"] = {
            'filter_range': str(cfg.filterRange),
            'downsampling_factor': str(cfg.dwnSample),
            'artifact_threshold': str(cfg.artifactThreshold),
            'onset': str(cfg.onset),
            'offset': str(cfg.offset),
            'sex': cfg.sex,
            'excel_sheet': cfg.excel_sheet,
            'condition' : str(cfg.condition),
            'batches': cfg.batches 
        }

        with open('continuous_config.ini', 'w') as f:
            config.write(f)

    def create_binary_config_file(self):
        config = configparser.ConfigParser()
        cfg = Config()

        config["DEFAULT"] = {
            'filter_range': str(cfg.filterRange),
            'downsampling_factor': str(cfg.dwnSample),
            'artifact_threshold': str(cfg.artifactThreshold),
            'onset': str(cfg.onset),
            'offset': str(cfg.offset),
            'sex': cfg.sex,
            'excel_sheet': cfg.excel_sheet,
            'batches': cfg.batches 
        }

        with open('binary_config.ini', 'w') as f:
            config.write(f)

    def update_continuous_config(self, config_file_path, config):
        parser = configparser.ConfigParser()
        parser.read(config_file_path)
        config.filterRange = eval(parser.get('DEFAULT', 'filter_range'))
        config.dwnSample = int(parser.get('DEFAULT', 'downsampling_factor'))
        config.artifactThreshold = float(parser.get('DEFAULT', 'artifact_threshold'))
        config.onset = float(parser.get('DEFAULT', 'onset'))
        config.offset = float(parser.get('DEFAULT', 'offset'))
        config.sex = parser.get('DEFAULT', 'sex')
        config.excel_sheet = parser.get('DEFAULT', 'excel_sheet')
        config.condition = parser.get('DEFAULT', 'condition')
        config.batches = 1

    def update_binary_config(self, config_file_path, config):
        parser = configparser.ConfigParser()
        parser.read(config_file_path)
        config.filterRange = eval(parser.get('DEFAULT', 'filter_range'))
        config.dwnSample = int(parser.get('DEFAULT', 'downsampling_factor'))
        config.artifactThreshold = float(parser.get('DEFAULT', 'artifact_threshold'))
        config.onset = float(parser.get('DEFAULT', 'onset'))
        config.offset = float(parser.get('DEFAULT', 'offset'))
        config.sex = parser.get('DEFAULT', 'sex')
        config.excel_sheet = parser.get('DEFAULT', 'excel_sheet')
        config.batches = 1

if __name__ == "__main__":
    # Initialize objects
    cfg = Config()
    controller = API_Controller()

    # Create a config file #
    # controller.create_config_file()

    # Apply changes made to the config file #
    controller.update_config("config.ini", cfg)
    print(cfg.sex)




