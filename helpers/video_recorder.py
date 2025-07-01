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
import datetime
import subprocess
import platform

# Identify the operating system
OS_TYPE = platform.system()

# Set FFmpeg path based on the downloaded version
FFMPEG_PATH = os.path.join(os.path.dirname(__file__), "..", "tools", "ffmpeg", "bin", "ffmpeg.exe" if OS_TYPE == "Windows" else "ffmpeg")

def get_ffmpeg_command(filename):
    # Define the FFmpeg command to start recording the screen
    if OS_TYPE == "Windows":
        return [
            FFMPEG_PATH, "-y", "-f", "gdigrab", "-framerate", "30", "-i", "desktop",
            "-c:v", "libx264", "-preset", "ultrafast", filename
        ]
    else:
        return [
            FFMPEG_PATH, "-y", "-f", "x11grab", "-framerate", "30", "-i", ":0.0",
            "-c:v", "libx264", "-preset", "ultrafast", filename
        ]

def start_ffmpeg_recording():
    # Generate a timestamp for the filename
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # Define the filename for the recording
    filename = f'recordings/videos/recording_{timestamp}.mpeg'
    # Create the directory for the recordings if it does not exist
    os.makedirs('recordings/videos', exist_ok=True)
    # Get the FFmpeg command
    command = get_ffmpeg_command(filename)
    # Start the FFmpeg process and return the process handle
    return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def stop_ffmpeg_recording(process):
    # Terminate the FFmpeg process
    process.terminate()
    # Wait for the process to finish
    process.wait()