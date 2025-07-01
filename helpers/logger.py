"""
selenium-python-behave-initial-project - Behave test framework with Selenium support
Copyright (C) 2025  Gábor Varga

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import logging
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

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

def log_to_console(message, status):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    formatted_message = f"{timestamp} - {message}"
    if status == 'passed':
        print(Fore.GREEN + formatted_message)
    elif status == 'failed':
        print(Fore.RED + formatted_message)
    elif status == 'in_progress':
        print(Fore.YELLOW + formatted_message)
    else:
        print(formatted_message)