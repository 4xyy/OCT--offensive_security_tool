import logging
import os

# Define log directory and filename
LOG_DIR = 'logs'
LOG_FILE = 'server.log'

# Create log directory if it doesn't exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Set up logger
server_logger = logging.getLogger('server_logger')
server_logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all log levels

# Create file handler for logging to a file
file_handler = logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE))
file_handler.setLevel(logging.DEBUG)  # Log all levels to file

# Create console handler for logging to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Log only INFO and above to console

# Define log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
server_logger.addHandler(file_handler)
server_logger.addHandler(console_handler)

# Avoid duplicated logs when using the same logger in different modules
server_logger.propagate = False
