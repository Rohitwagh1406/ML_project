from src.mlproject.logger import logging
from src.mlproject.exception import CustomeException
from src.mlproject.components.data_ingesion import DataIngstion
from src.mlproject.components.data_ingesion import DataIngestionConfig
import sys


if __name__ =="__main__":
    logging.info("The execution has started !")

    try:
        # data_ingesion_config=DataIngestionConfig()
        data_ingesion=DataIngstion()
        data_ingesion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomeException(e,sys)