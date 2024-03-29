from PIL import Image
from random import randint
import ctypes, os

#For all .jpg files in the containing folder, add those files to the list
img_dict = [f for f in os.listdir('.') if os.path.isfile(f) and 
	f[-4:]=='.jpg' and 
	f != 'cropped.jpg']
	
#acquire the 'absolute path' to cropped.jpg (e.g. C:\\Users\*user*\Desktop\Background_changer.py)
image_path = os.path.abspath('cropped.jpg')


img = Image.open(img_dict[randint(1, len(img_dict)-1)])
width, height = img.size

screen_width = 1366
screen_height = 768
top_left_x = randint(0, (width-screen_width))
top_left_y = randint(0, (height-screen_height))
croppedIm = img.crop(
	(top_left_x, top_left_y, 
	(top_left_x + screen_width)+1, 
	(top_left_y + screen_height)+1)
	)
croppedIm.save('cropped.jpg')

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(
	SPI_SETDESKWALLPAPER, 0, image_path, 0
	)


