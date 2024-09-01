import logging
import os
from datetime import datetime

# Correcting the LOG_FILE line
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H-%M_%S')}.log"

# Creating the logs directory and defining the full log file path
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Setting up the logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,           # Path to the log file
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
    level=logging.INFO,               # Log level
)

if __name__ == "__main__":
    logging.info("Logging has started")
 