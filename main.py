from Ensemble_cloth_Sales_prediction import logger
from Ensemble_cloth_Sales_prediction.pipeline.stage_01_data_injection import DataIngestionTrainingPipeLine
from Ensemble_cloth_Sales_prediction.pipeline.stage_02_data_preprocessing import DataPreprocessingTrainingPipeLine
from Ensemble_cloth_Sales_prediction.pipeline.stage_03_data_validation import DataValidationTrainingPipeLine
from Ensemble_cloth_Sales_prediction.pipeline.stage_04_data_splitting import DataSplittingTrainingPipeLine
from Ensemble_cloth_Sales_prediction.pipeline.stage_05_model_trainer import ModelTrainingPipeLine
from Ensemble_cloth_Sales_prediction.pipeline.stage_06_model_evaluation import ModelEvalPipeLine

"""
Data ingestion from the mySQL database 💉  
"""

STAGE_NAME = "Data Injection Stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataIngestionTrainingPipeLine()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

"""
Data preprocessing  ⚙️
"""

STAGE_NAME = "Data Preprocess Stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataPreprocessingTrainingPipeLine()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


""" Validating data to check if all required columns are present. ✅ or ❌"""

STAGE_NAME = "Data Validation Stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_validation = DataValidationTrainingPipeLine()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


""" Dataset splitting train and test 🪓"""

STAGE_NAME = "Data splitting Stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_validation = DataSplittingTrainingPipeLine()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

""" Model training Stage 🏃🏿‍♂️"""

STAGE_NAME = "Model training Stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_validation = ModelTrainingPipeLine()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


""" Model Evaluation Stage 🏃🏿‍♂️"""

STAGE_NAME = "Model Evaluation Stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_validation = ModelEvalPipeLine()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
