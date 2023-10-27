# python3 -m venv QR
# source QR/bin/activate
# pip install --upgrade pip


# https://github.com/guofei9987/blind_watermark
# pip install blind-watermark

'''
Как дискретное косинусное преобразование (DCT), 
так и разложение по сингулярным значениям (SVD) 
использовались в качестве математических инструментов 
для встраивания данных в изображение.
В DCT-области коэффициенты DCT модифицируются элементами
псевдослучайной последовательности действительных значений.
В домене SVD распространенным подходом является изменение
сингулярных значений с помощью сингулярных значений визуального водяного знака.

http://www.theparticle.com/documents/DCT-SVDpaperFINAL.pdf
https://peerj.com/articles/cs-1427/#
https://www.ijcsi.org/papers/IJCSI-10-3-1-223-230.pdf
'''

# # embed watermark into image:
# blind_watermark --embed --pwd 1234 img/2.jpg "watermark text" img/embedded.png

# # extract watermark from image:
# blind_watermark --extract --pwd 1234 --wm_shape 111 img/embedded.png


# pip install segno ## (for create QR)

# pip install qreader


# deactivate

#Embed watermark:

# from blind_watermark import WaterMark

# bwm1 = WaterMark(password_img=1, password_wm=1)
# bwm1.read_img('img/re2.png')
# wm = 'QR-код содержат сложную информ, чем просто text. Need used специальные форматы data: vCard, iCalendar.'
# bwm1.read_wm(wm, mode='str')
# bwm1.embed('img/embedded_text.png')
# len_wm = len(bwm1.wm_bit)
# print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))


# #Extract watermark:

# bwm1 = WaterMark(password_img=1, password_wm=1)
# wm_extract = bwm1.extract('img/embedded_text.jpg', wm_shape=len_wm, mode='str')
# print('Extract text = ', wm_extract)
# print('\n')






# import segno

# qr_name = "result.png" #"watermark_qrcode.png"

# qrcode = segno.make_qr("QR-код содержат сложную информ, чем просто text. Need used специальные форматы data: vCard, iCalendar.")
# # qrcode.save(f"img/{qr_name}", scale=2, border=1,)

# qrcode.save(
#     f"img/{qr_name}",
#     scale=2,
#     light="white",
#     dark="black",
#     data_dark="green",
# )


# # Изменяем размер qr-кода для возможности добавить bit-reverse

# from PIL import Image
# with Image.open("img/watermark_qrcode.png") as im:
# 	im = im.resize((128, 128)) # 64 и 256 требуют других размеров контейнер 
# 	# # сохранение картинки
# 	im.save("img/watermark_qrcode.png") 
	

"""
# # pip install pillow qrcode-artistic
# qrcode_rotated = qrcode.to_pil(
#     scale=1,
#     light="white",
#     dark="black",
#     data_dark="green",
# ).rotate(45, expand=True)
# qrcode_rotated.save(f"img/{qr_name}") # не смог извлечь текст из QR
"""


# from qreader import QReader
# import cv2


# # Create a QReader instance
# qreader = QReader()

# # Get the image that contains the QR code
# image = cv2.cvtColor(cv2.imread(f"img/{qr_name}"), cv2.COLOR_BGR2RGB)

# # Use the detect_and_decode function to get the decoded QR data
# decoded_text_before = qreader.detect_and_decode(image=image)
# print("\n\ndecoded text before = ", decoded_text_before)



# embed images
# embed watermark:

# from blind_watermark import WaterMark

# bwm1 = WaterMark(password_wm=1, password_img=1)
# # read original image
# bwm1.read_img('img/2.jpg')
# # read watermark
# # bwm1.read_wm('img/watermark_qrcode.png')
# bwm1.read_wm('img/corupt.png')
# # embed
# bwm1.embed('img/embedded_img.png')



# # Имитация атаки на контейнер с посланием

# from PIL import Image
# with Image.open("img/watermark_qrcode.png") as im:
# #     im.rotate(1).save("img/embedded_img.png") 
# # к повороту даже на 1 градус неустойчив (даже при сообщении "QR-код" и "QR")

# 	# area = (10, 100, 600, 700) # к случайным обрезаниям также неустойчив
# 	# cropped_img = im.crop(area)
# 	# cropped_img.save("img/embedded_img.png")

# 	im = im.resize((128, 128))
# 	# # сохранение картинки
# 	im.save("img/watermark_qrcode.png") 
# 	# неустойчив даже к малому изменению размера 1280x852 pixels -> 1200x850 






# Extract watermark:

# from PIL import Image
# im = Image.open('img/watermark_qrcode.png')
# width, height = im.size
width, height = 128, 128
# # print(f'{width, height}')

from blind_watermark import WaterMark
bwm1 = WaterMark(password_wm=1, password_img=1)
# notice that wm_shape is necessary
bwm1.extract(filename='img/embedded_img.png', wm_shape=(width, height), out_wm_name='img/extracted_img.png', )
# bwm1.extract(filename='img/embedded_img.jpg', wm_shape=(width, height), out_wm_name='img/extracted_img.png', )


# # Проверка
# # Create a QReader instance
from qreader import QReader
import cv2
qreader = QReader()

# Get the image that contains the QR code
# image = cv2.cvtColor(cv2.imread('img/extracted_img1.png'), cv2.COLOR_BGR2RGB)
image = cv2.cvtColor(cv2.imread('img/result.png'), cv2.COLOR_BGR2RGB)

# Use the detect_and_decode function to get the decoded QR data
decoded_text_after = qreader.detect_and_decode(image=image)
print("\n\nextracted_img text (after)= \n", decoded_text_after)


# if decoded_text_before == decoded_text_after:
# 	print("\nTrue")
# else:
# 	print("\nFalse")
