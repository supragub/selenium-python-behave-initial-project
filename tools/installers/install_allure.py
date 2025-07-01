import os
import sys
import shutil
import zipfile
import tarfile
import urllib.request
import platform

# Allure download links for each OS
ALLURE_URLS = {
    "Windows": "https://github.com/allure-framework/allure2/releases/download/2.32.2/allure-2.32.2.zip",
    "Linux": "https://github.com/allure-framework/allure2/releases/download/2.32.2/allure-2.32.2.tgz",
    "Darwin": "https://github.com/allure-framework/allure2/releases/download/2.32.2/allure-2.32.2.zip"  # macOS
}

# Allure storage location
ALLURE_DIR = os.path.join(os.path.dirname(__file__), "..", "allure")

BIN_DIR = os.path.join(ALLURE_DIR, "bin")

# Operating system identification
OS_TYPE = platform.system()

def install_allure():
    """Download and unpack Allure for the appropriate OS."""
    if not os.path.exists(ALLURE_DIR):
        os.makedirs(ALLURE_DIR)

    url = ALLURE_URLS.get(OS_TYPE)
    if not url:
        print(f"Unsupported operating system: {OS_TYPE}")
        sys.exit(1)

    file_ext = ".zip" if OS_TYPE in ["Windows", "Darwin"] else ".tgz"
    allure_archive = os.path.join(ALLURE_DIR, f"allure{file_ext}")

    print(f"Installing Allure report... ", end="", flush=True)
    urllib.request.urlretrieve(url, allure_archive)

    if file_ext == ".zip":
        with zipfile.ZipFile(allure_archive, "r") as zip_ref:
            zip_ref.extractall(ALLURE_DIR)
            extracted_dir = os.path.join(ALLURE_DIR, os.listdir(ALLURE_DIR)[0])
            for item in os.listdir(extracted_dir):
                s = os.path.join(extracted_dir, item)
                d = os.path.join(ALLURE_DIR, item)
                shutil.move(s, d)
            shutil.rmtree(extracted_dir)
    elif file_ext == ".tgz":
        with tarfile.open(allure_archive, "r:gz") as tar_ref:
            tar_ref.extractall(ALLURE_DIR)

    os.remove(allure_archive)

    print("Done.")

if __name__ == "__main__":
    install_allure()