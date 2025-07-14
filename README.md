# Initial BDD Test Automation Framework

## About the project

It is an initial BDD test framework that supports automation testing of websites on different browsers.

## Built with

[![Python][Python]][Python-url]
[![Selenium][Selenium]][Selenium-url]
[![Behave][Behave]][Behave-url]
[![Allure][Allure]][Allure-url]
[![Docker][Docker]][Docker-url]

## Prerequisites

### Install latest Python [Required for BDD framework]

Don't forget to add Python path to the environment variables.
Minimum requirements Python 3.9+

```
https://www.python.org/downloads/
```

### Install latest Java JDK [Required for Allure Report in Local Run]

Don't forget to add JAVA path to the environment variables.
Minimum requirements Java JDK 11+

```
https://www.oracle.com/java/technologies/downloads/
```

### Install and Run latest Docker Desktop [Required for Docker Tests Run]

```
https://www.docker.com/products/docker-desktop/
```

## Project Structure

```
selenium-python-behave-initial-project/
├── behave.ini                  # Configuration for Behave test runner
├── cleanup.py                  # Script to clean up test artifacts, logs, recordings, and reports
├── requirements.txt            # Python dependencies
├── runner_local.py             # Local test runner with tag and reporting options
├── runner_docker.py            # Docker test runner
├── start.py                    # Interactive script to launch tests or cleanup
├── Dockerfile                  # Docker build file for containerized test runs
├── docker-compose.yml          # Docker Compose config for test orchestration
├── LICENSE                     # License file
├── README.md                   # Project documentation
├── features/                   # BDD test files for Behave
│   ├── config.py               # Central test configuration
│   ├── environment.py          # Behave environment hooks
│   ├── example.feature         # Example feature file (Gherkin syntax)
│   └── steps/                  # Step definitions
│       └── example.py          # Example step definitions
├── helpers/                    # Utility modules
│   ├── browser_initialiser.py  # Browser setup and teardown
│   ├── logger.py               # Logging functionality
│   ├── screenshot_recorder.py  # Screenshot capture
│   └── video_recorder.py       # Video recording
├── logs/                       # Log files
│   ├── behave.log              # Behave test execution log
│   ├── ffmpeg.log              # FFmpeg log
│   └── requirements.log        # Dependency installation log
├── recordings/                 # Media captured during test runs
│   ├── screenshots/            # Saved screenshots
│   └── videos/                 # Video recordings
├── reports/                    # Generated test reports (e.g., Allure)
├── tools/                      # Third-party tools and installers
│   ├── allure/                 # Allure reporting tool binaries
│   ├── ffmpeg/                 # FFmpeg binaries
│   └── installers/             # Install scripts for Allure and FFmpeg
└── pages/                      # (Optional) Page Object Model classes
```

## Getting Started

### 1. Clone Bitbucket repository

```
git clone https://github.com/supragub/selenium-python-behave-initial-project.git
```

### 2. Configure Test Framework

The `features/config.py` file contains parameters related to automated testing. The available configuration options are:

```
BASE_URL - Define the base URL for the tests
BROWSER - Define the browser to use for the tests (chrome, firefox, edge, safari)
WINDOW_SIZE - Define the window size for the browser in widthxheight format (eg. 1920x1080)
VIDEO_RECORDING - Define the video recording settings (True/False)
SCREENSHOT_RECORDING - Define the screenshot recording settings (True/False)
ALLURE_REPORT - Define the Allure report works (True/False)
DOCKER_BROWSER_OPTIONS - Define the list of arguments for Docker Run (eg. --headless)
LOCAL_BROWSER_OPTIONS - Define the list of arguments for Local Run (eg. --headless)
```

### 3. Run the Project locally with Python

Start Automation Test Framework
```
python start.py
```
```
Initial BDD Automation Test Framework

1. Run all tests
2. Run custom tests
3. Clean up test results (logs, recordings, reports)
4. Clean up all (test artifacts & environment data)
0. Exit

Enter the number of your choice:
```
Or you can run commands directly:

Build virtual environment and install tools (if necessary) and run tests
```
python runner_local.py                                      # Run all tests
python runner_local.py regression                           # Run a single test
python runner_local.py "regression or uat"                  # Run tests with OR connection
python runner_local.py "regression and smoke"               # Run tests with AND connection 
python runner_local.py "not uat"                            # Run tests with exclude
python runner_local.py "(regression or uat) and not smoke"  # Run tests with complex expression
```

Clean up test results (logs, recordings, reports)
```
python cleanup.py
```

Clean up all (test artifacts & environment data)
```
python cleanup.py all
```

### 4. Run the Project with Docker

You can also run the tests in a Docker container. This is useful for CI/CD pipelines or to ensure a consistent environment.

```
docker compose up
```

Test results and reports will be available in the `logs` and `reports` folders on your host machine.


[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

[Python-url]: https://www.python.org/

[Selenium]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white

[Selenium-url]: https://www.selenium.dev

[Behave]: https://img.shields.io/badge/Behave-802045?style=for-the-badge&logo=python&logoColor=white

[Behave-url]: https://behave.readthedocs.io/en/latest/

[Allure]: https://img.shields.io/badge/Allure-ff5000?style=for-the-badge&logo=allure&logoColor=white

[Allure-url]: https://allurereport.org/

[Docker]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=1D63ED&color=1D63ED

[Docker-url]: https://www.docker.com/