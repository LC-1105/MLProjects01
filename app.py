from src.mlproject.logger import logging

from src.mlproject.exception import CustomException
import sys

from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig

from src.mlproject.components.data_transformation import DataTransformation,DataTransformationConfig 

from src.mlproject.components.model_trainer import ModelTrainer,ModelTrainerConfig

if __name__=="__main__":
    logging.info("the execution has started")
    
    try:
        #a=1/0
        #data_ingestion_congig=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        #Data Transformation
        data_transformation =DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        
        #Model Training
        model_trainer=ModelTrainer()
        r2,modelname=model_trainer.initiate_model_trainer(train_arr,test_arr)
        print(r2, " ",modelname)
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)