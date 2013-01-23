#!/usr/bin/env python
import os
from PIL import Image

for filename in os.listdir('.'):
    image = Image.open(filename)
    width, height = image.size
    half_width = int(width / 2.0)
    # left, upper, right, lower
    left_box = (0, 0, half_width, height)
    left = image.crop(left_box)
    right_box = (half_width, 0, width, height)
    right = image.crop(right_box)
    filename = filename.replace('.jpg', '')
    left.save(filename + "-left.jpg", "JPEG", quality=92)
    right.save(filename + "-right.jpg", "JPEG", quality=92)
