# Initial BDD Automation Framework

This is an initial BDD framework that supports automation testing of websites on different browsers using Selenium, Python and Behave.

## Prerequisites:

### Install latest Python [Required for BDD framework]

Don't forget to add Python path to the environment variables.

```
https://www.python.org/downloads/
```

### Install latest Java JDK [Required for Allure Report in Local Run]

Don't forget to add JAVA path to the environment variables.

```
https://www.oracle.com/java/technologies/downloads/
```

### Install latest Scoop

Download Scoop

```
https://scoop.sh/
```

Open a PowerShell terminal (version 5.1 or later) and run this command:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

### Install latest Allure [Required for Allure Report in Local Run]

```
scoop install allure
```

### Install latest FFmpeg [Required for Video recording]

```
scoop install ffmpeg
```

### Install and Run latest Docker Desktop [Required for Docker Tests Run]

```
https://www.docker.com/products/docker-desktop/
```

### Install and Run latest PowerShell Core [Required for Linux]

```
sudo apt-get update
sudo apt-get install -y wget apt-transport-https software-properties-common
wget -q "https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb"
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update
sudo apt-get install -y powershell
```

## Getting Started

### Clone Bitbucket repository

```
git clone https://github.com/supragub/selenium-python-behave-initial-project.git
```

### Testing framework setup

The `features/config.py` file contains parameters related to automated testing. The available configuration options are:

```
BASE_URL - Define the base URL for the tests
BROWSER - Define the browser to use for the tests (chrome, firefox, edge, safari)
WINDOW_SIZE - Define the window size for the browser in widthxheight format (eg. 1920x1080)
VIDEO_RECORDING - Define the video recording settings (True/False)
SCREENSHOT_RECORDING - Define the screenshot recording settings (True/False)
DOCKER_BROWSER_OPTIONS - Define the list of arguments for Docker Run (eg. --headless)
LOCAL_BROWSER_OPTIONS - Define the list of arguments for Local Run (eg. --headless)
```

### Run tests in local

Windows:

```
powershell.exe -File start-local.ps1
```

### Run tests for Docker Desktop

Windows:

```
powershell.exe -File start-docker.ps1
```

Linux:

```
pwsh start-docker.ps1
```
