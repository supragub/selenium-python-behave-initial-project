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
from features import config
from helpers import browser_initialiser, logger, screenshot_recorder, video_recorder


def before_all(context):
    # initialize the browser
    browser_initialiser.setup_browser(context)

    # Open the website
    context.driver.get(config.BASE_URL)

    # Set window size for browser
    browser_initialiser.set_window_size(context.driver, config.WINDOW_SIZE)

    # Configure logging
    context.logger = logger.configure_logging()

    # Start FFmpeg recording if enabled
    if config.VIDEO_RECORDING:
        context.ffmpeg_process = video_recorder.start_ffmpeg_recording()


def after_all(context):
    # Releasing resources
    if hasattr(context, 'driver'):
        context.driver.quit()
    if hasattr(context, 'logger'):
        logger.log_end(context.logger)

    # Stop FFmpeg recording if enabled
    if hasattr(context, 'ffmpeg_process') and config.VIDEO_RECORDING:
        video_recorder.stop_ffmpeg_recording(context.ffmpeg_process)


def before_feature(context, feature):
    # Log the start of a feature
    message = f"START  -  FEATURE - {feature.name}"
    context.logger.info(message)
    logger.log_to_console(message, 'in_progress')

    # Delete all cookies and session storage
    context.driver.delete_all_cookies()
    context.driver.execute_script("window.sessionStorage.clear();")
    context.driver.execute_script("window.localStorage.clear();")


def after_feature(context, feature):
    # Log the end of a feature with its status
    status = 'PASSED' if feature.status == 'passed' else 'FAILED'    
    message = f"{status} -  FEATURE - {feature.name}"
    context.logger.info(message)
    logger.log_to_console(message, feature.status)
    context.logger.info("")


def before_scenario(context, scenario):
    # Log the start of a scenario
    message = f"START  - SCENARIO - {scenario.name}"
    context.logger.info(message)
    logger.log_to_console(message, 'in_progress')

    if "isolate" in scenario.tags:
        # Delete all cookies and session storage
        context.driver.delete_all_cookies()
        context.driver.execute_script("window.sessionStorage.clear();")
        context.driver.execute_script("window.localStorage.clear();")    


def after_scenario(context, scenario):
    # Log the end of a scenario with its status
    status = 'PASSED' if scenario.status == 'passed' else 'FAILED'
    message = f"{status} - SCENARIO - {scenario.name}"
    context.logger.info(message)
    logger.log_to_console(message, scenario.status)
    
    if "isolate" in scenario.tags:
        # Delete all cookies and session storage
        context.driver.delete_all_cookies()
        context.driver.execute_script("window.sessionStorage.clear();")
        context.driver.execute_script("window.localStorage.clear();")


def after_step(context, step):
    # Log the status of a step
    status = 'PASSED' if step.status == 'passed' else 'FAILED'    
    message = f"{status} -   STEP   - {step.keyword} {step.name}"
    context.logger.info(message)
    logger.log_to_console(message, step.status)

    # Take a screenshot if the step failed
    if step.status == 'failed':
        screenshot_recorder.take_screenshot(context.driver)
