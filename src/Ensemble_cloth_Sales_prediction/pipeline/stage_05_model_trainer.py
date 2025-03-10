# model trainer
import warnings  

from Ensemble_cloth_Sales_prediction.config.configuration import ConfigurationManager
from Ensemble_cloth_Sales_prediction.components.modelTrainer import ModelTrainer
from Ensemble_cloth_Sales_prediction import logger 

warnings.filterwarnings('ignore')

STAGE_NAME = "Data Model Trainer Stage"

class ModelTrainingPipeLine:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_Trainer_config = config.get_model_training()
        model_trainer = ModelTrainer(config=model_Trainer_config)
        model_trainer.train()
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeLine()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e