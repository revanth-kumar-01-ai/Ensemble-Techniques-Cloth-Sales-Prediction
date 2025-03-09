# configuration manager in src config
import warnings 

from Ensemble_cloth_Sales_prediction.constants import * 
from Ensemble_cloth_Sales_prediction.utils.common import read_yaml, create_directories
from Ensemble_cloth_Sales_prediction.entity.config_entity import (DataIngestionConfig, DataPreprocessingConfig)

# warnings ignore 
warnings.filterwarnings('ignore')

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):


        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)


        create_directories([self.config.artifacts_root])

    # data ingestion 💉
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion


        create_directories([config.root_dir])


        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_query=config.source_query,
            load_data=config.load_data,
        )


        return data_ingestion_config
    
    # data preprocessing 
    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        config = self.config.data_preprocessing

        create_directories([config.root_dir])

        data_preprocess_config = DataPreprocessingConfig(
            root_dir=config.root_dir,
            clothSalesDataset=config.clothSalesDataset,
            load_data=config.load_data,
            preprocessModel=config.preprocessModel
        )

        return data_preprocess_config