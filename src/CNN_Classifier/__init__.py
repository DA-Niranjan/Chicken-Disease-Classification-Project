"""
Creating a log file - helps in debuging code in development environment and deployment process as we would not get terminal while deploying code in the environment
"""

import os
import sys
import logging

# Define the logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory and file path for the log file
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_log.log")

# Create the directory if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Set up basic configuration for logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Log to file
        logging.StreamHandler(sys.stdout)   # Log to console
    ]
)

# Get the logger instance
logger = logging.getLogger("PLEASE_KEEP_NOTE")