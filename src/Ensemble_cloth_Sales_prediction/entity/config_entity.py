from dataclasses import dataclass 
from pathlib import Path 

# data ingestion 💉
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_query: str  
    load_data: Path

# data preprocessing 
@dataclass(frozen=True)
class DataPreprocessingConfig:
    root_dir: Path
    clothSalesDataset: Path
    load_data: Path
    preprocessModel: Path

# data validation 
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    cleanDataset: Path
    all_schema: dict

# data Splitting 
@dataclass(frozen=True)
class DataSplittingConfig:
    root_dir: Path
    cleanData: Path
    trainData: Path
    testData: Path

# model trainer 
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model: Path
    streamLitModel: Path

    # Decision tree 
    DTParams: dict

    # Random Forest 
    RFParams: dict

    # logistic regression params 
    LGParams: dict

    # Knn 
    KNNParams: dict

    # Target column
    target_column: str


# model evaluation
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model: Path # decision tree model 
    
    DFParams: dict # params
    RFParams: dict # params
    LGParams: dict # params
    KNNParams: dict # params
    
    metric_file_name: Path # model output 
    target_column: str # target column
    mlflow_uri: str 