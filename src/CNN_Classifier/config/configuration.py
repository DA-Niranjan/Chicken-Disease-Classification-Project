from CNN_Classifier.constants import *
from CNN_Classifier.utils.common import read_yaml, create_directories
from CNN_Classifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH, # From constant.py
                 params_filepath = PARAMS_FILE_PATH): # From constant.py 
        
        self.config = read_yaml(config_filepath) # assigns dict from config/config.yaml
        self.params = read_yaml(params_filepath) # assigns dict from param.yaml
        
        create_directories([self.config.artifacts_root]) #Creating artifact folder in root directory
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir]) #creating data_ingestion folder within a artifact directory
        
        # define return type of the function and store the values in a variable
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )
        
        return data_ingestion_config
