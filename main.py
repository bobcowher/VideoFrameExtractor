# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import cv2
import os

filename = sys.argv[1]

divider = filename.find(".")

name = filename[:divider]


print(f"Processing {filename}")

video = cv2.VideoCapture(filename)

fps = video.get(cv2.CAP_PROP_FPS)
print(f'Frames per second = {fps}')

frame_number = 0

output_dir = f"{name}_image_output"

# Ensure the directory structure exists.
try:
    os.mkdir(output_dir)
except:
    print(f"Directory {output_dir} already exists or could not be created")

# Loop through and process images.
try:
    while True:
        if frame_number % 1000 == 0:
            video.set(cv2.CAP_PROP_POS_MSEC, frame_number)
            ret, frame = video.read()
            cv2.imwrite(f'./{name}_image_output/{name}_frame_{frame_number}.png', frame)

            if frame_number % 100000 == 0:
                print(f"Processed {frame_number / 1000} images...")

        frame_number += 1

except:
    print(f"Completed writing {frame_number / 1000} images")



