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
from features import config

def create_directories():
    directories = ["logs", "recordings/screenshots", "reports"]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def run_tests(tags=None):
    print("Running tests in Docker...", flush=True)
    # Base tag setting to exclude skipped tests
    if tags:
        if isinstance(tags, str):
            if ' ' in tags:
                tag_list = ["--tags=-skip", f"--tags={tags}"]
            else:
                tag_list = ["--tags=-skip", f"--tags=@{tags}"]
        elif isinstance(tags, list):
            tags_combined = " or ".join(f"@{tag}" for tag in tags)
            tag_list = ["--tags=-skip", f"--tags={tags_combined}"]
    else:
        tag_list = ["--tags=-skip"]

    command = [
        sys.executable,
        "-m",
        "behave",
        *tag_list
    ]
    print(f"\nExecuting command: {' '.join(command)}")
    try:
        result = subprocess.run(command, check=True)
        print("")
    except subprocess.CalledProcessError as e:
        print("")

def main():
    create_directories()
    tags = None
    if len(sys.argv) > 1:
        tags = " ".join(sys.argv[1:])
    run_tests(tags)

if __name__ == "__main__":
    main()
