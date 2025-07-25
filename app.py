from src.mlproject.logger import logging
from src.mlproject.exception import CustomeException
from src.mlproject.components.data_ingesion import DataIngstion
from src.mlproject.components.data_ingesion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTranformationConfig, DataTransformation
import sys


if __name__ =="__main__":
    logging.info("The execution has started !")

    try:
        # data_ingesion_config=DataIngestionConfig()
        data_ingesion=DataIngstion()
        train_data_path, test_data_path = data_ingesion.initiate_data_ingestion()

        # data_transformation_config = data_transformation_config()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transormation(train_data_path, test_data_path)




    except Exception as e:
        logging.info("Custome Exception")
        raise CustomeException(e,sys)