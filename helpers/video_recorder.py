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


class VideoRecorder:
    """
    Handles screen video recording for Selenium test sessions using FFmpeg.
    Supports both Windows and Linux environments.
    """
    def __init__(self, output_dir='recordings/videos'):
        """
        Initialize the video recorder, set up FFmpeg path, and ensure output directory exists.
        """
        self.output_dir = output_dir
        self.os_type = platform.system()
        self.ffmpeg_path = os.path.join(
            os.path.dirname(__file__), "..", "tools", "ffmpeg", "bin",
            "ffmpeg.exe" if self.os_type == "Windows" else "ffmpeg"
        )
        self.process = None
        os.makedirs(self.output_dir, exist_ok=True)

    def _get_ffmpeg_command(self, filename):
        """
        Build the FFmpeg command for the current OS and target filename.
        """
        if self.os_type == "Windows":
            return [
                self.ffmpeg_path, "-y", "-f", "gdigrab", "-framerate", "30", "-i", "desktop",
                "-c:v", "libx264", "-preset", "ultrafast", "-maxrate", "8M", "-bufsize", "2M", filename
            ]
        else:
            return [
                self.ffmpeg_path, "-y", "-f", "x11grab", "-framerate", "30", "-i", ":0.0",
                "-c:v", "libx264", "-preset", "ultrafast", "-maxrate", "8M", "-bufsize", "2M", filename
            ]

    def start(self):
        """
        Start the FFmpeg process to record the screen. Returns the output filename.
        """
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = os.path.join(self.output_dir, f'recording_{timestamp}.mpeg')
        command = self._get_ffmpeg_command(filename)
        log_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'ffmpeg.log')
        log_path = os.path.abspath(log_path)
        log_file = open(log_path, 'w')
        self.process = subprocess.Popen(command, stdout=log_file, stderr=log_file)
        return filename

    def stop(self):
        """
        Stop the FFmpeg recording process and clean up.
        """
        if self.process:
            self.process.terminate()
            self.process.wait()
            self.process = None
