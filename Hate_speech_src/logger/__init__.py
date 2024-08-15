import os
import logging
from datetime import datetime

filename=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)

log_file_path=os.path.join(logs_path,filename)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s | module : %(name)s | %(levelname)s - %(message)s"
)

data_ingestion_logger=logging.getLogger("data_ingestion")
data_transformation_logger=logging.getLogger("data_transformation")
model_trainer_logger=logging.getLogger("model_trainer")
model_evaluation_logger=logging.getLogger("model_evaluation")
model_pusher_logger=logging.getLogger("model_pusher")