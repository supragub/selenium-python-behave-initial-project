import os
import sys
import shutil
import zipfile
import tarfile
import urllib.request
import platform

# FFmpeg download links for each os
FFMPEG_URLS = {
    "Windows": "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip",
    "Linux": "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz",
    "Darwin": "https://evermeet.cx/ffmpeg/getrelease"  # macOS
}

# FFmpeg storage location
FFMPEG_DIR = os.path.join(os.path.dirname(__file__), "..", "ffmpeg")

BIN_DIR = os.path.join(FFMPEG_DIR, "bin")

# Operating system identification
OS_TYPE = platform.system()

def install_ffmpeg():
    """Download and unpack FFmpeg for the appropriate OS."""
    if not os.path.exists(FFMPEG_DIR):
        os.makedirs(FFMPEG_DIR)

    url = FFMPEG_URLS.get(OS_TYPE)
    if not url:
        print(f"Unsupported operating system: {OS_TYPE}")
        sys.exit(1)

    file_ext = ".zip" if OS_TYPE == "Windows" else ".tar.xz" if OS_TYPE == "Linux" else ".zip"
    ffmpeg_archive = os.path.join(FFMPEG_DIR, f"ffmpeg{file_ext}")

    print(f"Installing FFmpeg video recorder... ", end="", flush=True)
    urllib.request.urlretrieve(url, ffmpeg_archive)

    if file_ext == ".zip":
        with zipfile.ZipFile(ffmpeg_archive, "r") as zip_ref:
            zip_ref.extractall(FFMPEG_DIR)
            extracted_dir = os.path.join(FFMPEG_DIR, os.listdir(FFMPEG_DIR)[0])
            for item in os.listdir(extracted_dir):
                s = os.path.join(extracted_dir, item)
                d = os.path.join(FFMPEG_DIR, item)
                shutil.move(s, d)
            shutil.rmtree(extracted_dir)
    elif file_ext == ".tar.xz":
        with tarfile.open(ffmpeg_archive, "r:xz") as tar_ref:
            tar_ref.extractall(FFMPEG_DIR)

    os.remove(ffmpeg_archive)

    print("Done.")

if __name__ == "__main__":
    install_ffmpeg()