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
import datetime
import allure


class ScreenshotRecorder:
    """
    Handles screenshot capture and file management for Selenium test sessions.
    Screenshots are saved with scenario and step context, and can be attached to reports.
    """
    def __init__(self, screenshots_dir=None):
        """
        Initialize the screenshot recorder and ensure the target directory exists.
        """
        self.screenshots_dir = screenshots_dir or os.path.join('recordings', 'screenshots')
        os.makedirs(self.screenshots_dir, exist_ok=True)

    def take_screenshot(self, context):
        """
        Capture a screenshot using the Selenium context and attach it to the Allure report.
        """
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'recordings/screenshots/screenshot_{timestamp}.png'

        context.driver.save_screenshot(filename)

        with open(filename, "rb") as f:
            allure.attach(f.read(), name=f"Screenshot", attachment_type=allure.attachment_type.PNG)
