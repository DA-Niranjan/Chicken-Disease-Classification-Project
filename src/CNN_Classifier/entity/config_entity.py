from dataclasses import dataclass #Define the custom data type of return of the functions
from pathlib import Path

@dataclass(frozen=True) #Setting (frozen=True) makes the instance immutable
class DataIngestionConfig:
    # dir: Data type => this will come from config.yaml
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path 
    
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path : Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int