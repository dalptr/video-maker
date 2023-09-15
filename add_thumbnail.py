import subprocess
import os

frame_rate = 30
duration = 2
input_file = 'asset/videos/input.mp4'
output_file = input_file + '_with_thumbnail.mp4'
thumbnail_file = 'asset/images/thumbnail.jpg'

assert os.path.exists(input_file)
assert os.path.exists(thumbnail_file)
user_settings = f'ffmpeg -framerate {frame_rate} -loop 1 -t {duration} -i {thumbnail_file} -i {input_file}'
default_settings = ' -filter_complex "[0:v] [1:v] concat=n=2:v=1 [v]" -map "[v]" -map 1:a -c:v libx264 -crf 18 -c:a aac -strict experimental '
command_str = user_settings + default_settings + output_file
subprocess.call(command_str, shell=True)
