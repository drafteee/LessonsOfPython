from PIL import Image
import sys
import os

image_Folder1 = './scripting/photos/'
image_Folder2 = './scripting/photos_new/'

if not os.path.exists(image_Folder2):
    os.makedirs(image_Folder2)

print(os.path.exists(image_Folder2))

for filename in os.listdir(image_Folder1):
    img = Image.open(f'{image_Folder1}{filename}')
    clean_name = os.path.splitext(filename)
    img.save(f'{image_Folder2}{clean_name[0]}.png', 'png')
