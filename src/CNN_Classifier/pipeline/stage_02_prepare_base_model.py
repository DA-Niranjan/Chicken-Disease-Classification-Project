from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.prepare_base_model import PrepareBaseModel
from CNN_Classifier import logger

STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


#For dvc.yaml file
if __name__ == '__main__':
    try:
        logger.info(f"{'*'*8}")
        logger.info(f"{'>'*8} stage {STAGE_NAME} started {'<'*8}")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"{'>'*8} stage {STAGE_NAME} completed {'<'*8}\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e