# python3 -m venv QR
# source QR/bin/activate


# Изменяем размер 

from PIL import Image
with Image.open("2.png") as im:
	width, height = im.size
	k = 3
	im = im.resize((int(width/k), int(height/k))) 
	im.save("re2.png") 