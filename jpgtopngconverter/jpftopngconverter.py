import os  # we can use the pathlib module also
import sys
from PIL import Image
# grab first and second argument
img_folder = sys.argv[1]
output_folder = sys.argv[2]

print(img_folder)
print(output_folder)

# check if new exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through poke_images
# convert images from jpg to png
# save to new folder
for filename in os.listdir(img_folder):
    img = Image.open(f'{img_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done')

# Sample terminal command:- python3 jpgtopngconverter.py poke_images/ new/
