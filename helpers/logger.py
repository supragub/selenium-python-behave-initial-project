import logging


def setup_logging(log_file_path):
    # Create a file handler for logging
    handler = logging.FileHandler(log_file_path, encoding='utf-8')
    handler.setLevel(logging.INFO)
    # Set the format for log messages
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

    # Get the logger instance for 'behave'
    logger = logging.getLogger('behave')
    logger.setLevel(logging.INFO)
    # Add the file handler to the logger
    logger.addHandler(handler)
    return logger


def configure_logging():
    # Define the path for the log file
    log_file_path = 'logs/behave.log'
    # Create or clear the log file
    open(log_file_path, 'w').close()
    # Set up logging with the specified log file path
    logger = setup_logging(log_file_path)
    # Log the start of the test execution
    log_start(logger)
    return logger


def log_start(logger):
    # Log the start of the test execution
    logger.info("TESTS EXECUTION STARTED.")
    logger.info("")


def log_end(logger):
    # Log the end of the test execution
    logger.info("TESTS EXECUTION COMPLETED.")
    # Shut down the logging system
    logging.shutdown()
