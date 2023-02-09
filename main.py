'''
Написать программу генерации монохромной BMP-картинки на основе вашего варианта.
'''

import struct
from bmp_format import *


print(F_FORMAT_STR + BMP_FILE_HDR_STR)
print(F_FORMAT_STR + BMP_FILE_HDR_STR + BMP_INFO_HDR_STR)
print(F_FORMAT_STR + BMP_FILE_HDR_STR + BMP_INFO_HDR_STR + BMP_COLOR_TABLE_STR)
# Открытие файла изображения для записи
fd_out = open('img.bmp', 'wb');




# Закрытие файла изображения
fd_out.close();