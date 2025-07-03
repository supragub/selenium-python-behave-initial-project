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
from features import config
from helpers.browser_initialiser import BrowserInitializer
from helpers.logger import Logger
from helpers.screenshot_recorder import ScreenshotRecorder
from helpers.video_recorder import VideoRecorder


def before_all(context):
    # Initialize helpers as objects
    context.browser_initializer = BrowserInitializer(config)
    context.logger = Logger()
    context.screenshot_recorder = ScreenshotRecorder()
    context.video_recorder = None

    # Initialize the browser
    context.browser_initializer.setup_browser(context)
    context.driver.get(config.BASE_URL)
    context.browser_initializer.set_window_size(context.driver, config.WINDOW_SIZE)

    # Start FFmpeg recording if enabled and not running in Docker
    if config.VIDEO_RECORDING and not os.getenv('RUNNING_IN_DOCKER'):
        context.video_recorder = VideoRecorder()
        context.video_recorder.start()


def after_all(context):
    # Releasing resources
    if hasattr(context, 'driver'):
        context.driver.quit()
    if hasattr(context, 'logger'):
        context.logger.log_end()

    # Stop FFmpeg recording if enabled and not running in Docker
    if context.video_recorder and config.VIDEO_RECORDING and not os.getenv('RUNNING_IN_DOCKER'):
        context.video_recorder.stop()


def before_feature(context, feature):
    # Log the start of a feature
    message = f"START  -  FEATURE - {feature.name}"
    context.logger.logger.info(message)
    context.logger.log_to_console(message, 'in_progress')

    # Delete all cookies and session storage
    context.driver.delete_all_cookies()
    context.driver.execute_script("window.sessionStorage.clear();")
    context.driver.execute_script("window.localStorage.clear();")


def after_feature(context, feature):
    # Log the end of a feature with its status
    status = 'PASSED' if feature.status == 'passed' else 'FAILED'
    message = f"{status} -  FEATURE - {feature.name}"
    context.logger.logger.info(message)
    context.logger.log_to_console(message, feature.status)
    context.logger.logger.info("")


def before_scenario(context, scenario):
    # Log the start of a scenario
    message = f"START  - SCENARIO - {scenario.name}"
    context.logger.logger.info(message)
    context.logger.log_to_console(message, 'in_progress')

    if "isolate" in scenario.tags:
        # Delete all cookies and session storage
        context.driver.delete_all_cookies()
        context.driver.execute_script("window.sessionStorage.clear();")
        context.driver.execute_script("window.localStorage.clear();")


def after_scenario(context, scenario):
    # Log the end of a scenario with its status
    status = 'PASSED' if scenario.status == 'passed' else 'FAILED'
    message = f"{status} - SCENARIO - {scenario.name}"
    context.logger.logger.info(message)
    context.logger.log_to_console(message, scenario.status)

    if "isolate" in scenario.tags:
        # Delete all cookies and session storage
        context.driver.delete_all_cookies()
        context.driver.execute_script("window.sessionStorage.clear();")
        context.driver.execute_script("window.localStorage.clear();")


def after_step(context, step):
    # Log the status of a step
    status = 'PASSED' if step.status == 'passed' else 'FAILED'
    message = f"{status} -   STEP   - {step.keyword} {step.name}"
    context.logger.logger.info(message)
    context.logger.log_to_console(message, step.status)

    # Take a screenshot if the step failed
    if step.status == 'failed':
        context.screenshot_recorder.take_screenshot(context)
