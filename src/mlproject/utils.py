# used to create generic functionalities

import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd

import pickle
import numpy as np

def read_data():
    logging.info("Rading the dataset")
    try:
        df= pd.read_csv("Datasets_for_Project.csv")
        print(df.head())
        
    except Exception as e:
        raise CustomException(e,sys)
    
    return df

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)      
#The Pickle dump() and dumps() functions are used to serialize an object. The only difference between them is 
# that dump() writes the data to a file, while dumps() represents it as a byte object. 
#“wb” mode. This means that you are writing the file in binary mode so that the data is returned in a bytes object.
#Similarly, load() reads pickled objects from a file, whereas loads() deserializes them from a bytes-like object. 
#we unpickle the object using the load() function
           
    except Exception as e:
        raise CustomException(e,sys)