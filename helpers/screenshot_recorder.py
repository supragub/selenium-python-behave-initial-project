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


def take_screenshot(context):
    # Create a directory for screenshots if it doesn't exist
    if not os.path.exists('recordings/screenshots'):
        os.makedirs('recordings/screenshots')

    # Generate a filename with the current timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'recordings/screenshots/screenshot_{timestamp}.png'

    # Take the screenshot and save it
    context.save_screenshot(filename)

    # Attach the screenshot to the Allure report
    with open(filename, "rb") as f:
        allure.attach(f.read(), name=f"Screenshot", attachment_type=allure.attachment_type.PNG)