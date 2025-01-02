import os
import datetime
import subprocess


def start_ffmpeg_recording():
    # Generate a timestamp for the filename
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # Define the filename for the recording
    filename = f'recordings/videos/recording_{timestamp}.mpg'
    # Create the directory for the recordings if it does not exist
    if not os.path.exists('recordings/videos'):
        os.makedirs('recordings/videos')
    # Define the FFmpeg command to start recording the screen
    command = [
        'ffmpeg', '-y', '-f', 'gdigrab', '-framerate', '30', '-i', 'desktop',
        '-c:v', 'libx264', '-r', '30', filename
    ]
    # Start the FFmpeg process and return the process handle
    return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def stop_ffmpeg_recording(process):
    # Terminate the FFmpeg process
    process.terminate()
    # Wait for the process to complete
    process.wait()
