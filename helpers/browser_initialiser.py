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
import os
import tempfile
from features import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


class BrowserInitializer:
    """
    Handles browser initialization and configuration for Selenium tests.
    Supports Chrome, Firefox, and Edge. Applies environment-specific options.
    """
    def __init__(self, config):
        self.config = config

    def setup_browser(self, context):
        """
        Initializes the Selenium WebDriver for the configured browser and attaches it to the context.
        """
        browser_name = self.config.BROWSER_NAME.lower()
        options = self.get_browser_options(browser_name)
        driver = None
        if browser_name == 'chrome':
            service = ChromeService()
            driver = webdriver.Chrome(options=options, service=service)
        elif browser_name == 'firefox':
            service = FirefoxService()
            driver = webdriver.Firefox(options=options, service=service)
        elif browser_name == 'edge':
            service = EdgeService()
            driver = webdriver.Edge(options=options, service=service)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        context.driver = driver
        return driver

    def get_browser_options(self, browser):
        """
        Returns the appropriate browser options object with all required arguments for the environment.
        """
        if browser == 'chrome':
            options = ChromeOptions()
        elif browser == 'firefox':
            options = FirefoxOptions()
        elif browser == 'edge':
            options = EdgeOptions()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        if os.getenv('RUNNING_IN_DOCKER'):
            for arg in self.config.DOCKER_BROWSER_OPTIONS:
                options.add_argument(arg)
            if browser == 'chrome':
                tmp_dir = tempfile.mkdtemp(prefix="chrome-user-data-")
                options.add_argument(f"--user-data-dir={tmp_dir}")
        else:
            for arg in self.config.LOCAL_BROWSER_OPTIONS:
                options.add_argument(arg)
        return options

    @staticmethod
    def set_window_size(driver, size):
        """
        Sets the browser window size based on a 'WIDTHxHEIGHT' string.
        """
        width, height = map(int, size.split('x'))
        driver.set_window_size(width, height)
