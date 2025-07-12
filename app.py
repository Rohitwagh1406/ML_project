from src.mlproject.logger import logging
from src.mlproject.exception import CustomeException
import sys


if __name__ =="__main__":
    logging.info("The execution has started !")

    try:
        a=1/0
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomeException(e,sys)