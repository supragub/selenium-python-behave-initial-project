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


class Logger:
    """
    Logger class for test execution logging and colored console output.
    Handles log file creation, start/end markers, and status-based console messages.
    """
    def __init__(self, log_file_path='logs/behave.log', logger_name='behave'):
        """
        Initialize the logger, clear the log file, and log the start of execution.
        """
        self.log_file_path = log_file_path
        self.logger_name = logger_name
        self.logger = self._setup_logger()
        self._clear_log_file()
        self.log_start()

    def _setup_logger(self):
        """
        Set up the Python logging.FileHandler and return the logger instance.
        """
        handler = logging.FileHandler(self.log_file_path, encoding='utf-8')
        handler.setLevel(logging.INFO)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.INFO)
        if not logger.hasHandlers():
            logger.addHandler(handler)
        return logger

    def _clear_log_file(self):
        """
        Create or clear the log file before test execution.
        """
        open(self.log_file_path, 'w').close()

    def log_start(self):
        """
        Log the start of test execution.
        """
        self.logger.info("TESTS EXECUTION STARTED.")
        self.logger.info("")

    def log_end(self):
        """
        Log the end of test execution and shut down logging.
        """
        self.logger.info("TESTS EXECUTION COMPLETED.")
        logging.shutdown()

    @staticmethod
    def log_to_console(message, status):
        """
        Print a colored console message based on test status (passed, failed, in_progress, etc.).
        """
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
