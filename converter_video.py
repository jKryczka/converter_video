# TO DO
# implement auto detection of files
# implement file deletion
# implement handling of vertical files
#
#
#
#
#
#
#



import ffmpeg
import sys


input_file = 'input.mp4'
output_file = 'output_resized.mp4'


new_width = 1920
new_height = 1080

(
    ffmpeg
    .input(input_file)
    .filter('scale', width=new_width, height=new_height)
    .output(output_file)
    .run()
)