import os 
import pandas as pd

from Ensemble_cloth_Sales_prediction import logger
from Ensemble_cloth_Sales_prediction.entity.config_entity import ModelTrainerConfig

# models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# stacking 
from  sklearn.ensemble import StackingClassifier

import joblib


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # decision tree 
        modelDT = DecisionTreeClassifier(
            max_depth = self.config.DTParams['max_depth'], 
            min_samples_leaf = self.config.DTParams['min_samples_leaf'],
            min_samples_split = self.config.DTParams['min_samples_split'], 
        )

        modelDT.fit(train_x, train_y)
        logger.info("Decision Tree model successfully built.")

        # Random Fores 
        modelRF = RandomForestClassifier(
            max_depth =  self.config.RFParams['max_depth'], 
            min_samples_leaf = self.config.RFParams['min_samples_leaf'],
            min_samples_split = self.config.RFParams['min_samples_split'], 
            n_estimators = self.config.RFParams['n_estimators'], 
        )

        modelRF.fit(train_x, train_y)
        logger.info("Random Forest model successfully built.")

        # Logistic Regression  
        modelLG = LogisticRegression(
            C =  self.config.LGParams['C'], 
            solver = self.config.LGParams['solver']
        )

        modelLG.fit(train_x, train_y)
        logger.info("Logistic Regression model successfully built.")

        # Knn neighbors
        modelKnn = KNeighborsClassifier(
            metric =  self.config.KNNParams['metric'], 
            n_neighbors = self.config.KNNParams['n_neighbors']
        )

        modelKnn.fit(train_x, train_y)
        logger.info("Knn neighbors model successfully built.")

        # estimators 
        estimators = [
            ('Random Forest',  modelRF),
            ('Decision Tree', modelDT),
            ('lg', modelLG),
            ('knn', modelKnn),
        ]

        # meta model
        meta_model = LogisticRegression()
    
        # stacking
        stackModel = StackingClassifier(estimators = estimators, final_estimator = meta_model)

        # model training 
        stackModel.fit(train_x, train_y)
        logger.info("Stacking model with RF, DT, LG, and KNN successfully built.")

        # save model
        joblib.dump(stackModel, self.config.model)