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
from cleanup import cleanup, CleanupMode

def main():
    while True:
        print("\nInitial BDD Automation Test Framework\n")
        print("1. Run all tests")
        print("2. Run custom tests")        
        print("3. Run regression tests")
        print("4. Run user acceptance tests")
        print("5. Clean up test results (logs, recordings, reports)")
        print("6. Clean up all (test artifacts & environment data)")
        print("0. Exit")

        choice = input("\nEnter the number of your choice: ").strip()

        if choice == "1":
            os.system("python runner.py")
        elif choice == "2":
            print("\nExamples of tag usage:")
            print("- Single tag: regression")
            print("- Multiple tags with OR: regression or uat")
            print("- Multiple tags with AND: regression and smoke")
            print("- Excluding tags: not skip")
            print("- Complex expression: (regression or uat) and not skip")
            tags = input("\nPlease enter the tags for test execution: ").strip()
            if tags:
                # Quotes ensure complex expressions work correctly
                os.system(f'python runner.py "{tags}"')
            else:
                print("\nNo tags provided, returning to main menu.")
        elif choice == "3":
            os.system("python runner.py regression")
        elif choice == "4":
            os.system("python runner.py uat")
        elif choice == "5":
            cleanup(CleanupMode.TEST_RESULTS)
        elif choice == "6":
            cleanup(CleanupMode.ALL)
        elif choice == "0":
            print("\nExit.")
            break
        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()
