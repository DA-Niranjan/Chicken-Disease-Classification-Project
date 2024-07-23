from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.evaluation import Evaluation
from CNN_Classifier import logger

STAGE_NAME = "Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
        

#For dvc.yaml file        
if __name__ == "__main__":
    try:
        logger.info(f"{'*'*8}")
        logger.info(f"{'>'*8} stage {STAGE_NAME} started {'<'*8}")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"{'>'*8} stage {STAGE_NAME} completed {'<'*8}\n\nx================x")
    
    except Exception as e:
        logger.exception(e)
        raise e
