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
import shutil
import time
from enum import Enum, auto

class CleanupMode(Enum):
    """Cleanup modes for the framework"""
    TEST_RESULTS = auto()  # Clean only test results
    ALL = auto()           # Clean everything including environment

# Directories to clean for test results only
TEST_RESULTS_DIRS = [
    os.path.join("logs"),
    os.path.join("recordings"),
    os.path.join("reports")
]

# Additional directories to clean for full cleanup
ENVIRONMENT_DIRS = [
    os.path.join("tools", "ffmpeg"),
    os.path.join("tools", "allure"),
    os.path.join("features", "__pycache__"),
    os.path.join("helpers", "__pycache__"),
    os.path.join("pages", "__pycache__"),
    os.path.join("__pycache__")
]

VENV_DIR = ".venv"

def remove_venv():
    """Remove virtual environment directory with retry mechanism"""
    if os.path.exists(VENV_DIR):
        print("Removing virtual environment... ", end='', flush=True)
        try:
            shutil.rmtree(VENV_DIR)
            print("Done.")
        except Exception as e:
            print(f"Failed to delete {VENV_DIR}. Reason: {e}")
            time.sleep(1)
            try:
                shutil.rmtree(VENV_DIR)
                print("Retry successful: Virtual environment deleted.")
            except Exception as e:
                print(f"Retry failed. Reason: {e}")

def clear_directory(directory):
    """Clear a single directory"""
    if os.path.exists(directory):
        try:
            shutil.rmtree(directory)
            os.makedirs(directory, exist_ok=True)  # Recreate empty directory
        except Exception as e:
            print(f"Failed to process {directory}. Reason: {e}")

def cleanup(mode=CleanupMode.TEST_RESULTS):
    """Perform cleanup based on specified mode"""
    # Always clean test results directories
    for directory in TEST_RESULTS_DIRS:
        clear_directory(directory)
    
    if mode == CleanupMode.ALL:
        # Clean additional directories for full cleanup
        for directory in ENVIRONMENT_DIRS:
            clear_directory(directory)
        remove_venv()
        print("\nAll test artifacts and environment data successfully cleared.")
    else:
        print("\nTest results successfully cleared.")

def main():
    """Command line interface for cleanup"""
    import sys
    mode = CleanupMode.ALL if len(sys.argv) > 1 and sys.argv[1].lower() == "all" else CleanupMode.TEST_RESULTS
    cleanup(mode)

if __name__ == "__main__":
    main()