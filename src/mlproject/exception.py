import sys #Built-in functions, exceptions, and other objects.
from src.mlproject.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()   #Traceback info
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):#Exception: Common base class for all exceptions
    def __init__(self, error_message,error_details:sys) : # Constructor or Initializer                                                
        super().__init__(error_message)  
        #The super() function is often used with the __init__() method to initialize the attributes of the parent class. 
        self.error_message=error_message_detail(error_message,error_details)
            
    def __str__(self) : #Return str(self). # __str__ is to print() the value
        return self.error_message
                                                


# class Emp():
    #def __init__(self, id, name, Add):
         # self.id = id
         # self.name = name
         # self.Add = Add
    
# Class freelancer inherits EMP
#class Freelance(Emp):
    #def __init__(self, id, name, Add, Emails):
        #  super().__init__(id, name, Add)
        #  self.Emails = Emails
        