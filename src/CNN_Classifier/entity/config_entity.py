from dataclasses import dataclass #Define the custom data type of return of the functions
from pathlib import Path

@dataclass(frozen=True) #Setting (frozen=True) makes the instance immutable
class DataIngestionConfig:
    # dir: Data type => this will come from config.yaml
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path 