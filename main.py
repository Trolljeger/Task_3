'''
Написать программу генерации монохромной BMP-картинки на основе вашего варианта.
'''

import struct
import math
from bmp_format import *


class BmpWriter:
    '''
    Класс для записи BMP файла изображения
    '''


    def set_img_name(self, img_name):
        '''
        функция установки имени изображения
        :param img_name: имя изображения. Имя файла img_name.bmp
        :return: ...
        '''
        if (type(img_name) != str):
            raise TypeError(
                f'Неверный тип входных данных. \n'
                f'Ожидаемый формат img_name == > str'
            )

        self.file_name = img_name + '.bmp'
        print(f'Имя файла: {self.file_name}')


    def set_data(self, img_data, width, heigth):
        '''
        Функция установки данных изображения
        :param img_data: массив значений изображения list[[[r,g,b] size of width] size of heigth]
        :param width: ширина изображения >= 100
        :param heigth: высота изображения >= 100
        :return: ...
        '''

        # Проверка соответствия типов входных параметров конструктора
        if (type(width) != int or type(heigth) != int):
            raise TypeError(
                f'Неверный тип входных данных. \n'
                f'Ожидаемый формат width == > int, heigth ==> int. \n'
            )

        if width < 100 or heigth < 100 or len(img_data) != width or len(img_data[0]) != heigth or len(img_data[0][0]) != 3:
            raise ValueError(
                f'Неверный размер входных данных. \n'
                f'Размер изображения не менне 100 \n'
            )

        self.bmp_width = width
        self.bmp_heigth = heigth
        self.bmp_matrix = img_data

        print(f'Img size ==> {self.bmp_width} x {self.bmp_heigth}')

    def save_file(self):

        # Вычисляем размер файла
        self.file_size = 14 + 40 + 3 * self.bmp_width * self.bmp_heigth

        # фомируем заголовок BMP файла
        self.bmp_header = struct.pack(BMP_FILE_HDR_STR, 0x4D42, self.file_size, 0, 0, 54)
        self.bmp_info = struct.pack(BMP_INFO_HDR_STR, 40, self.bmp_width, self.bmp_heigth, 1, 24, 0, 0, 0, 0, 0, 0)

        self.img_array = bytearray()
        for i in range(0, self.bmp_width):
            for j in range(0, self.bmp_heigth):
                self.img_array += struct.pack('=BBB', *self.bmp_matrix[i][j])

            for j in range(self.bmp_heigth % 4):
                self.img_array += struct.pack('=B', 0)


        with open(self.file_name, 'wb') as bmp_file:

            # записываем данные в файл
            bmp_file.write(self.bmp_header)
            bmp_file.write(self.bmp_info)
            bmp_file.write(self.img_array)


def prepare_data(img_data, width, heigth):
    '''
    Функция подготовки данных для записи в файл
    :param img_data: массив для формирования данных изображения
    :param width: ширина изображения (int)
    :param heigth: длина изображения (int)
    :return: заполненный массив значений
    '''

    img_data = [[[255, 255, 255] for i in range(0, width)] for j in range(0, heigth)]

    step = 1 / width
    phase = 0.0
    while phase < 2.0 * math.pi:
        x = int((width / 2 - 1) * ((math.sin(3.0 * phase + math.pi / 2.0) + 1)))
        y = int((heigth / 2 - 1) * ((math.sin(2.0 * phase) + 1)))
        img_data[x][y] = [0, 0, 0]
        phase += step

    return img_data



# параметры отображения
dim = 1000
bmp_name = 'result_img'

# массив данных изображения
bmp_data = None

try:
    bwr = BmpWriter()
    bwr.set_img_name(bmp_name)

    # Заполняем данные изображения
    bmp_data = prepare_data(bmp_data, dim, dim)

    # передаем а запись в файл
    bwr.set_data(bmp_data, dim, dim)

    # записываем в файл
    bwr.save_file()
except Exception as ex:
    print(type(ex))
    print(ex)

