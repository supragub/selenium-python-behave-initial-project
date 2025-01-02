import os
import datetime


def take_screenshot(browser):
    # Create a directory for screenshots if it doesn't exist
    if not os.path.exists('recordings/screenshots'):
        os.makedirs('recordings/screenshots')

    # Generate a filename with the current timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'recordings/screenshots/screenshot_{timestamp}.png'

    # Take the screenshot and save it
    browser.save_screenshot(filename)
    print(f'Screenshot saved as {filename}')
