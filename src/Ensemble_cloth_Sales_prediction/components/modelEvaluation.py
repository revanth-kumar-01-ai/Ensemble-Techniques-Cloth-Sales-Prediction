import warnings 
from pathlib import Path
import os
import pandas as pd

from Ensemble_cloth_Sales_prediction.utils.common import save_json
from Ensemble_cloth_Sales_prediction.entity.config_entity import ModelEvaluationConfig
from Ensemble_cloth_Sales_prediction import logger 

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import joblib
import dagshub
import mlflow
from datetime import datetime

warnings.filterwarnings('ignore')

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self, actual, pred):

        # accuracy 
        acc = accuracy_score(y_pred = pred, y_true = actual)

        # precision
        precision = precision_score(y_pred = pred, y_true = actual)

        # recall
        recall = recall_score(y_pred = pred, y_true = actual)

        # f1 score
        f1 = f1_score(y_pred = pred, y_true = actual)
        return acc, precision, recall, f1
    
    
    def log_stacking_model_mlflow(self):

        

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model)
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Dagshub
        dagshub.init(repo_owner='revanth-kumar-01-ai', repo_name='Ensemble-Techniques-Cloth-Sales-Prediction', mlflow=True)
        mlflow.set_experiment('Stacking Model') # Experiment Name

        run_name = f"StackingModel_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)

            (acc, precision, recall, f1) = self.eval_metrics(test_y, predicted_qualities)

            scores = {"accuracy_score": acc, "precision_score": precision, "recall_score": recall, "f1": f1}

            save_json(path=Path(os.path.join(self.config.metric_file_name, "stacking_model.json")), data=scores)

            mlflow.log_params(self.config.DFParams)
            mlflow.log_metric("accuracy_score", acc)
            mlflow.log_metric("precision_score", precision)
            mlflow.log_metric("recall_score", recall)
            mlflow.log_metric("f1", f1)
            logger.info(f"MLflow run '{run_name}' successfully created.")
        