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


def setup_browser(context):
    # Get the browser name from the configuration and convert it to lowercase
    browser_name = config.BROWSER_NAME.lower()
    # Get the browser-specific options
    options = get_browser_options(browser_name)

    if browser_name == 'chrome':
        # Set up the ChromeDriver service with the log file
        service = ChromeService()
        # Initialize the Chrome browser with the specified options and service
        context.driver = webdriver.Chrome(options=options, service=service)

    elif browser_name == 'firefox':
        # Set up the GeckoDriver service with the log file
        service = FirefoxService()
        # Initialize the Firefox browser with the specified options and service
        context.driver = webdriver.Firefox(options=options, service=service)

    elif browser_name == 'edge':
        # Set up the EdgeDriver service with the log file
        service = EdgeService()
        # Initialize the Edge browser with the specified options and service
        context.driver = webdriver.Edge(options=options, service=service)

    print()


def get_browser_options(browser):
    # Return the appropriate options object based on the browser name
    if browser == 'chrome':
        options = ChromeOptions()

    elif browser == 'firefox':
        options = FirefoxOptions()

    elif browser == 'edge':
        options = EdgeOptions()

    else:
        raise ValueError(f"Unsupported browser: {browser}")


    # Check if the code is running inside a Docker container
    if os.getenv('RUNNING_IN_DOCKER'):
        for arg in config.DOCKER_BROWSER_OPTIONS:
            options.add_argument(arg)
        # Add a unique user-data-dir for Chrome to avoid session conflicts
        if browser == 'chrome':
            tmp_dir = tempfile.mkdtemp(prefix="chrome-user-data-")
            options.add_argument(f"--user-data-dir={tmp_dir}")
    else:
        for arg in config.LOCAL_BROWSER_OPTIONS:
            options.add_argument(arg)

    return options


def set_window_size(driver, size):
    width, height = map(int, size.split('x'))
    driver.set_window_size(width, height)


# if __name__ == "__main__":
#     # initialize the browser
#     browser_initialiser.setup_browser(context)

#     # Open the website
#     context.driver.get(config.BASE_URL)

#     # Set window size for browser
#     browser_initialiser.set_window_size(context.driver, config.WINDOW_SIZE)
