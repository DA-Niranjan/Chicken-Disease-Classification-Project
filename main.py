# Endpoint file

from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"

if __name__ == '__main__':
    try:
        logger.info(f"{'>'*8} stage {STAGE_NAME} started {'<'*8}")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"{'>'*8} stage {STAGE_NAME} completed {'<'*8}\n\nx================x")
        
    except Exception as e:
        logger.exception(e)
        raise e