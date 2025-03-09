# Data preprocessing 
from pathlib import Path  
import os 

import pandas as pd  

from Ensemble_cloth_Sales_prediction import logger  
from Ensemble_cloth_Sales_prediction.utils.common import get_size
from Ensemble_cloth_Sales_prediction.entity.config_entity import DataPreprocessingConfig  

from feature_engine.outliers import Winsorizer


class DataPreprocessing:
    def __init__(self, config: DataPreprocessingConfig):
        self.config = config

    def load_dataset(self):
        df = pd.read_csv(self.config.clothSalesDataset)
        return df
    
    def preprocessingDataset(self, df):

        # outliers 
        outliers = Winsorizer(tail = 'both', capping_method = 'iqr', fold = 1.5, variables = ['Price', 'CompPrice', 'Sales'])
        df[['Price', 'CompPrice', 'Sales']] = outliers.fit_transform(df[['Price', 'CompPrice', 'Sales']])

        # binning
        df['Sales'] = pd.qcut(df['Sales'], q=2, labels=['Low', 'High'])

        # replace the column
        df['Sales'] = df.pop('Sales')

        df = pd.get_dummies(df, drop_first = True).astype(int)

        # rename the Sales_High to target 
        df.rename(columns={'Sales_High': 'target'}, inplace=True)

        if not os.path.exists(self.config.load_data):
            
            df.to_csv(self.config.load_data, index=False)
            logger.info(f"{self.config.load_data} successfully preprocessed. Saved as cleanDataset.csv")

        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.load_data))}")