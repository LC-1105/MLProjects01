import os
from pathlib import Path
#Pathlib module in Python provides various classes representing file system paths with semantics 
#appropriate for different operating systems.
#The os.path module is always the path module suitable for the operating system Python is running on,
# and therefore usable for local paths.

import logging
logging.basicConfig(level=logging.INFO)

project_name='mlproject'

list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "application.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
    
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename= os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
        #os.mkdir() is used to create a single directory, and it raises an error if the parent directory
        # doesn’t exist.This method raises FileExistsError if the directory to be created already exists.
        #os.makedirs() creates parent directories as needed, allowing the creation of nested directories,
        #and it doesn’t raise an error if the directories already exist.
        
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        #Test whether a path exists       Return the size of a file, reported by os.stat()
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")