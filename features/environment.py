import os
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
    if config.VIDEO_RECORDING and not os.getenv('RUNNING_IN_DOCKER'):
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
    context.logger.info(f"FEATURE - {feature.name} - IN PROGRESS...")


def after_feature(context, feature):
    # Log the end of a feature with its status
    context.logger.info(f"FEATURE - {feature.name} - {feature.status}")
    context.logger.info("")


def before_scenario(context, scenario):
    # Log the start of a scenario
    context.logger.info(f"SCENARIO - {scenario.name} - IN PROGRESS...")


def after_scenario(context, scenario):
    # Log the end of a scenario with its status
    context.logger.info(f"SCENARIO - {scenario.name} - {scenario.status}")


def after_step(context, step):
    # Log the status of a step
    context.logger.info(f"STEP - {step.name} - {step.status}")

    # Take a screenshot if the step failed
    if step.status == 'failed':
        screenshot_recorder.take_screenshot(context.driver)
