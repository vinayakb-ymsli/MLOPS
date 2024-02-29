import logging as log
from datetime import date
import sys
from datetime import datetime
import time
import os

'''Description : logger 
@author : Aryan
@dev : logger file can be used to create a logger configuration which can be imported and used in other files.
in other files it will be used by logger.log.
'''
#FILE/FOLDER CONFIGURATION
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#CONFIGURE LOGGING FORMAT
today = str(date.today())
filename=LOG_FILE_PATH
log.basicConfig( format=' %(asctime)s | [%(levelname)s] | %(lineno)d | %(name)s | %(message)s',  datefmt="%Y-%m-%dT%H:%M:%S%z",level=log.INFO,handlers=[log.FileHandler(filename),log.StreamHandler(sys.stdout)])


#TEST MESSAGE
if __name__ =="__main__":
    log.info("test")
