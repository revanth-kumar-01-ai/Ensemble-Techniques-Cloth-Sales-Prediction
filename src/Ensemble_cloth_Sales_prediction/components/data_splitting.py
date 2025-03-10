import pandas as pd 

from Ensemble_cloth_Sales_prediction import logger
from Ensemble_cloth_Sales_prediction.entity.config_entity import DataSplittingConfig

from sklearn.model_selection import train_test_split

class DataSplitting:
    def __init__(self, config: DataSplittingConfig):
        self.config = config

    def load_Data(self):
        return pd.read_csv(self.config.cleanData)
    
    def train_test_spiting(self, data):
        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data, test_size = 0.3, random_state = 42, stratify = data['target'])

        train.to_csv(self.config.trainData, index = False)
        test.to_csv(self.config.testData ,index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
