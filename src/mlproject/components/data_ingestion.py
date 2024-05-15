# Source>Load data>train test split 
import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.mlproject.utils import read_data
from sklearn.model_selection import train_test_split

#from src.mlproject.components.data_ingestion import DataIngestion
#from src.mlproject.components.data_ingestion import DataIngestionConfig

from src.mlproject.components.data_transformation import DataTransformation,DataTransformationConfig 
from src.mlproject.components.model_trainer import ModelTrainer,ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join('artifacts','raw.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
            
    
    def initiate_data_ingestion(self):
        try:
            df=read_data()
            logging.info("Loading the data")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            #dirname=Returns the directory component of a pathname
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Data Ingestion is completed")
            
            return (self.ingestion_config.train_data_path, 
                    self.ingestion_config.test_data_path)
        
        except Exception as e:
            raise CustomException(e,sys)       
        
        
if __name__=="__main__":
    #Data_ingestion
    data_ingestion=DataIngestion()
    train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()

    #Data Transformation
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    #Model Training
    modeltrainer=ModelTrainer()
    r2,modelname=modeltrainer.initiate_model_trainer(train_arr,test_arr)
    print(modelname, " : ",r2)
    