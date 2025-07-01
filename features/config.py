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
# Define the base URL for the tests

BASE_URL = "https://www.selenium.dev/"


# Define the browser to use for the tests
# Browser options:
# chrome
# firefox
# edge

BROWSER_NAME = 'chrome'


# Define the window size for the browser in widthxheight format
# Common screen resolutions:
# 3840x2160 (4K, UHD)
# 2560x1440 (2K, QHD)
# 1920x1080 (Full HD)
# 1366x768 (HD)
# 1440x900 (WXGA+)
# 1536x864 (HD+)
# 1280x720 (HD)
# Common mobile resolutions (below HD):
# 360x640 (WVGA)
# 375x667 (iPhone 6/7/8)
# 414x736 (iPhone 6/7/8 Plus)
# 360x780 (Pixel 4a)
# 360x760 (Pixel 5)

WINDOW_SIZE = '1920x1080'


# Define the video recording settings
# On Windows systems with multiple screens in extended mode, video recording may not work correctly.
# It is recommended to use only one screen, which can be in duplicated mode if needed.

VIDEO_RECORDING = True


# Define the screenshot recording settings

SCREENSHOT_RECORDING = True


# Define the Allure riport settings
# True: Enable Allure riport after test execution
# False: Disable Allure riport after test execution

ALLURE_REPORT = True


# Define the list of arguments for Docker Run
# Common browser options:
# --headless: Run browser in headless mode
# --no-sandbox: Disable the sandbox for all process types that are normally sandboxed
# --disable-dev-shm-usage: Disable /dev/shm usage
# --disable-gpu: Disable GPU hardware acceleration
# --incognito: Open browser in incognito mode
# --disable-extensions: Disable all extensions

DOCKER_BROWSER_OPTIONS = [
    "--headless",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu"
]


# Define the list of arguments for Local Run
# Common browser options:
# --headless: Run browser in headless mode
# --no-sandbox: Disable the sandbox for all process types that are normally sandboxed
# --disable-dev-shm-usage: Disable /dev/shm usage
# --disable-gpu: Disable GPU hardware acceleration
# --incognito: Open browser in incognito mode
# --disable-extensions: Disable all extensions
LOCAL_BROWSER_OPTIONS = [

]
