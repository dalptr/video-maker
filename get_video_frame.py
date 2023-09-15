import subprocess

video = "input.mp4"
frame = "frame.jpg"
time = "00:00:12"
command = f"ffmpeg -i {video} -ss {time} -frames:v 1 {frame}"
subprocess.call(command, shell=True)
