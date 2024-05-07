"""
 setup.py is a module used to build and distribute Python packages. It typically contains information 
 about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package. 
 This information is used by the pip tool, which is a package manager for Python that allows users to install 
 and manage Python packages from the command line. 
 By running the setup.py file with the pip tool, you can build and distribute your Python package 
 so that others can use it..

to run it use following command: python setup.py install
OR
-e .= put in requirements.txt. everytime requirements.txt run, it will by default trigger setup.py

"""

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:
    """
    this function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()  # read line by line readlines return type : list[str]
        requirements=[req.replace("\n","") for req in requirements] # replace newline \n with blank spaces
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
    


setup(
    name="mlproject",
    version="0.1",
    author="Lalit",
    packages=find_packages(),  # find all the packages; packages=['my_package'] kindly provide the name of the packages in list format
    install_requires= get_requirements("requirements.txt")
)