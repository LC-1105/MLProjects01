# used to create generic functionalities

import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd

def read_data():
    logging.info("Rading the dataset")
    try:
        df= pd.read_csv("Datasets_for_Project.csv")
        print(df.head())
        
    except Exception as e:
        raise CustomException(e,sys)
    
    return df