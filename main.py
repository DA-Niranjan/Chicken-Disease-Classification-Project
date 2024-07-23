# Endpoint file

from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from CNN_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNN_Classifier.pipeline.stage_03_training import ModelTrainingPipeline
from CNN_Classifier.pipeline.stage_04_evaluation import EvaluationPipeline



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"{'>'*8} stage {STAGE_NAME} started {'<'*8}")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"{'>'*8} stage {STAGE_NAME} completed {'<'*8}\n\nx================x")
    
except Exception as e:
    logger.exception(e)
    raise e
    

STAGE_NAME = "Prepare base model"

try:
    logger.info(f"{'*'*8}")
    logger.info(f"{'>'*8} stage {STAGE_NAME} started {'<'*8}")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f"{'>'*8} stage {STAGE_NAME} completed {'<'*8}\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e
    
    
STAGE_NAME = "Training"

try:
    logger.info(f"{'*'*8}")
    logger.info(f"{'>'*8} stage {STAGE_NAME} started {'<'*8}")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"{'>'*8} stage {STAGE_NAME} completed {'<'*8}\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation stage"

try:
    logger.info(f"{'*'*8}")
    logger.info(f"{'>'*8} stage {STAGE_NAME} started {'<'*8}")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f"{'>'*8} stage {STAGE_NAME} completed {'<'*8}\n\nx================x")

except Exception as e:
    logger.exception(e)
    raise e
