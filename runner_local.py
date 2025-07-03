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
import sys
import subprocess
import platform
import webbrowser
from features import config

VENV_DIR = ".venv"
LOG_DIR = "logs"
REQUIREMENTS_LOG = os.path.join(LOG_DIR, "requirements.log")
FFMPEG_PATH = os.path.join("tools", "ffmpeg", "bin")
ALLURE_PATH = os.path.join("tools", "allure", "bin")


def venv_exists():
    return os.path.isdir(VENV_DIR)


def create_venv():
    print("Creating virtual environment... ", end='', flush=True)
    try:
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
        print("Done.")
    except subprocess.CalledProcessError as e:
        print(f"Failed. Reason: {e}")


def get_venv_python():
    return os.path.join(VENV_DIR, "Scripts" if platform.system() == "Windows" else "bin", "python")


def create_directories():
    directories = [LOG_DIR, "recordings/screenshots", "recordings/videos", "reports"]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def install_requirements(python_path):
    pip_path = python_path.replace("python", "pip")
    print("Checking dependencies... ", end='', flush=True)
    os.makedirs(LOG_DIR, exist_ok=True)
    try:
        with open(REQUIREMENTS_LOG, "w") as log_file:
            subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True, stdout=log_file, stderr=log_file)
        print("Done.")
    except subprocess.CalledProcessError as e:
        print(f"Failed. Reason: {e}")


def install_ffmpeg():
    if config.VIDEO_RECORDING and not os.path.exists(FFMPEG_PATH):
        subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "tools", "installers", "install_ffmpeg.py")], check=True)


def install_allure():
    if config.ALLURE_REPORT and not os.path.exists(ALLURE_PATH):
        subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "tools", "installers", "install_allure.py")], check=True)


def run_tests(python_path, tags=None):
    print("Running tests... ", end='', flush=True)

    # Base tag setting to exclude skipped tests
    if tags:
        if isinstance(tags, str):
            # If string contains spaces, it's a complex expression
            if ' ' in tags:
                # For complex expressions, combine with -skip
                tag_list = [f"--tags=-skip", f"--tags={tags}"]
            else:
                # For simple tags, combine with -skip
                tag_list = [f"--tags=-skip", f"--tags=@{tags}"]
        elif isinstance(tags, list):
            # For list of tags, combine with OR operator
            tags_combined = " or ".join(f"@{tag}" for tag in tags)
            tag_list = [f"--tags=-skip", f"--tags={tags_combined}"]
    else:
        tag_list = ["--tags=-skip"]

    if config.ALLURE_REPORT:
        command = [
            python_path,
            "-m", 
            "behave",
            *tag_list,
            "-f",
            "allure_behave.formatter:AllureFormatter", 
            "-o",
            "reports"
        ]
    else:
        command = [
            python_path,
            "-m",
            "behave",
            *tag_list
        ]
    
    # Ensuring the virtual environment explicitly
    env = os.environ.copy()
    env["PATH"] = os.path.join(VENV_DIR, "Scripts") + os.pathsep + env["PATH"]

    try:
        result = subprocess.run(command, check=True, stdout=sys.stdout, stderr=sys.stderr, env=env)
        print("")
    except subprocess.CalledProcessError as e:
        print("")


def open_reports():
    if config.ALLURE_REPORT:
        allure_executable = os.path.join(os.path.dirname(__file__), "tools", "allure", "bin", "allure")
        if os.name == 'nt':
            allure_executable += ".bat"
        reports_path = os.path.join(os.path.dirname(__file__), "reports")
        subprocess.run([allure_executable, "serve", reports_path], shell=True)
        webbrowser.open("http://localhost:4040")  # Replace '4040' with the actual port number used by Allure


def main():
    if not venv_exists():
        create_venv()
    python_path = get_venv_python()
    create_directories()
    install_requirements(python_path)
    install_ffmpeg()
    install_allure()
    
    # Command line argument processing
    tags = None
    if len(sys.argv) > 1:
        # If there's only one argument, pass it as a string
        # If there are multiple arguments, combine them with spaces
        tags = " ".join(sys.argv[1:])
    
    run_tests(python_path, tags)
    open_reports()

if __name__ == "__main__":
    main()
