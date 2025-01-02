# Define the base URL for the tests

BASE_URL = "https://selenium.dev/"


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

VIDEO_RECORDING = True


# Define the screenshot recording settings

SCREENSHOT_RECORDING = True


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
