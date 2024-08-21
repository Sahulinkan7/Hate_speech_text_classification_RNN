from Hate_speech_src.logger import logging,data_ingestion_logger,data_transformation_logger,model_trainer_logger

from Hate_speech_src.exceptions import HateSpeechException
import sys 
from Hate_speech_src.configuration.gcloud_syncer import GcloudSyncer

data_ingestion_logger.info("Data ingestion started")

# try:
#     print(4/0)
# except Exception as e:
#     data_ingestion_logger.error(str(HateSpeechException(e,sys)))
#     raise HateSpeechException(e,sys) from e

data_transformation_logger.info("data transformation started")

obj=GcloudSyncer()
data_ingestion_logger.info(f"downloading data from google cloud")
obj.sync_folder_from_gcloud(gcp_bucket_url="nlp-hate-speech-data",filename="dataset.zip",destination="downloads")
data_ingestion_logger.info(f"data downloaded successfully!")