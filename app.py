from src.mlproject.logger import logging
from src.mlproject.exception import CustomeException
from src.mlproject.components.data_ingesion import DataIngstion
from src.mlproject.components.data_ingesion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTranformationConfig, DataTransformation
from src.mlproject.components.model_tranier import ModelTrainerConfig,ModelTrainer
import sys


if __name__ =="__main__":
    logging.info("The execution has started !")

    try:
        # data_ingesion_config=DataIngestionConfig()
        data_ingesion=DataIngstion()
        train_data_path, test_data_path = data_ingesion.initiate_data_ingestion()

        # data_transformation_config = data_transformation_config()
        data_transformation = DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

        ## Model Training

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))





    except Exception as e:
        logging.info("Custome Exception")
        raise CustomeException(e,sys)