from PIL import Image, ImageFilter
import sys
import os

#grab the first and second arguements
source_images_path = sys.argv[1]
converted_images_path = sys.argv[2]

#check if converted_images_path exists, if not create
if not os.path.exists(converted_images_path):
	os.makedirs(converted_images_path)

#Loop though all images given and convert them to png
images = os.listdir(source_images_path)
for image in images:
	image_path = f"{source_images_path}/{image}"
	img = Image.open(image_path)
	png_name = image.replace('.jpg','.png')
	img.save(f"{converted_images_path}/{png_name}", 'png')
