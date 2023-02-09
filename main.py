'''
Написать программу генерации монохромной BMP-картинки на основе вашего варианта.
'''

import struct
import math
from bmp_format import *

# параметры отображения
dim = 1003
bmp_width = dim
bmp_heigth = dim

bmp_matrix = [[[255, 255, 255] for i in range(0, dim)] for j in range(0, dim)]

step = 1/dim
phase = 0.0
while phase < 2.0 * math.pi :
    x = int((dim/2-1) * ((math.sin(3.0*phase + math.pi/2.0) + 1)))
    y = int((dim/2-1) * ((math.sin(2.0 * phase) + 1)))
    bmp_matrix[x][y] = [0, 0, 0]
    phase += step

file_size = 14 + 40 + 3 * dim *dim

# фомируем заголовок BMP файла
bmp_header = struct.pack(BMP_FILE_HDR_STR, 0x4D42, file_size, 0, 0, 54)
bmp_info = struct.pack(BMP_INFO_HDR_STR, 40, dim, dim, 1, 24, 0, 0, 0, 0, 0, 0)

img_array = bytearray()
for i in range(0, dim):
    for j in range(0, dim):
        img_array += struct.pack('=BBB', *bmp_matrix[i][j])

    for j in range(dim % 4) :
        img_array += struct.pack('=B', 0)


# Открытие файла изображения для записи
fd_out = open('img.bmp', 'wb');
fd_out.write(bmp_header)
fd_out.write(bmp_info)
fd_out.write(img_array)
# Закрытие файла изображения
fd_out.close()