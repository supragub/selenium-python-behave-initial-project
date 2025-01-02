import os
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
        # Create a log file for ChromeDriver
        with open('logs/chromedriver.log', 'w'):
            pass
        # Set up the ChromeDriver service with the log file
        service = ChromeService(log_path='logs/chromedriver.log')
        # Initialize the Chrome browser with the specified options and service
        context.driver = webdriver.Chrome(options=options, service=service)

    elif browser_name == 'firefox':
        # Create a log file for GeckoDriver
        with open('logs/geckodriver.log', 'w'):
            pass
        # Set up the GeckoDriver service with the log file
        service = FirefoxService(log_path='logs/geckodriver.log')
        # Initialize the Firefox browser with the specified options and service
        context.driver = webdriver.Firefox(options=options, service=service)

    elif browser_name == 'edge':
        # Create a log file for EdgeDriver
        with open('logs/edgedriver.log', 'w'):
            pass
        # Set up the EdgeDriver service with the log file
        service = EdgeService(log_path='logs/edgedriver.log')
        # Initialize the Edge browser with the specified options and service
        context.driver = webdriver.Edge(options=options, service=service)


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

    else:
        for arg in config.LOCAL_BROWSER_OPTIONS:
            options.add_argument(arg)

    return options


def set_window_size(driver, size):
    width, height = map(int, size.split('x'))
    driver.set_window_size(width, height)
