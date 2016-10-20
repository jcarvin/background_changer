from PIL import Image
from random import randint
import ctypes

img_dict = {
    1: 'The Garden Of Earthly Delights; Bosch.jpg',
    2: 'Last_judgement_Bosch.jpg',
    3: 'pieter_bruegel_i-fall_of_rebel_angels_merge.jpg',
    4: 'Bosch_-_Haywain_Triptych.jpg',
    5: '8635e209c80721f0dcda7d1e2be32918.jpg',
    6: 'Temptation_of_Saint_Anthony.jpg',
    7: '5a8450034be3a68da7a3dca779d5fc2a.jpg'
}

img = Image.open(img_dict[randint(1, len(img_dict))])
width, height = img.size

screen_width = 1366
screen_height = 768
top_left_x = randint(0, (width-screen_width))
top_left_y = randint(0, (height-screen_height))
croppedIm = img.crop((top_left_x, top_left_y, (top_left_x+screen_width)+1, (top_left_y+screen_height)+1))
croppedIm.save('cropped.jpg')

image_path = 'C:\\GitHub\\background_changer\cropped.jpg'
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)


