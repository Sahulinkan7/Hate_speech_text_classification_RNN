from Hate_speech_src.logger import logging,data_ingestion_logger,data_transformation_logger,model_trainer_logger

from Hate_speech_src.exceptions import HateSpeechException
import sys 

data_ingestion_logger.info("Data ingestion started")

try:
    print(4/0)
except Exception as e:
    data_ingestion_logger.error(str(HateSpeechException(e,sys)))
    raise HateSpeechException(e,sys) from e

data_transformation_logger.info("data transformation started")