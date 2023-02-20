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

    def  __init__(self, img_name, bmp_dim):
        '''
        Конструктор объекта
        :param: img_name - название изображения
        :param: dim - размерность изображения (dim x dim) Не менее 100
        '''


        # Проверка соответствия типов входных параметров конструктора
        if (type(img_name) != str or type(bmp_dim) != int or bmp_dim < 100):
            raise TypeError(
                f'Неверный тип входных данных. \n'
                f'Ожидаемый формат img_name == > str, bmp_dim ==> int. \n'
                f'Размер изображения не менне 100 \n'
                f'Ошибка создания объекта.'
            )


        self.file_name = img_name + '.bmp'
        self.bmp_width = bmp_dim
        self.bmp_heigth = bmp_dim
        self.bmp_matrix = [[[255, 255, 255] for i in range(0, bmp_dim)] for j in range(0, bmp_dim)]

        print(f'Output file name ==> {self.file_name}. Img size ==> {self.bmp_width} x {self.bmp_heigth}')


    def __prepare_data__(self):
        '''
        Функция подготовки данных для записи в файл
        '''

        # Вычисляем размер файла
        file_size = 14 + 40 + 3 * self.bmp_width * self.bmp_heigth

        # фомируем заголовок BMP файла
        self.bmp_header = struct.pack(BMP_FILE_HDR_STR, 0x4D42, file_size, 0, 0, 54)
        self.bmp_info = struct.pack(BMP_INFO_HDR_STR, 40, self.bmp_width, self.bmp_heigth, 1, 24, 0, 0, 0, 0, 0, 0)

        step = 1/self.bmp_width
        phase = 0.0
        while phase < 2.0 * math.pi :
            x = int((self.bmp_width/2-1) * ((math.sin(3.0*phase + math.pi/2.0) + 1)))
            y = int((self.bmp_width/2-1) * ((math.sin(2.0 * phase) + 1)))
            self.bmp_matrix[x][y] = [0, 0, 0]
            phase += step

        self.img_array = bytearray()
        for i in range(0, self.bmp_width):
            for j in range(0, self.bmp_heigth):
                self.img_array += struct.pack('=BBB', *self.bmp_matrix[i][j])

            for j in range(self.bmp_heigth % 4):
                self.img_array += struct.pack('=B', 0)


    def save_file(self):
        with open(self.file_name, 'wb') as bmp_file:

            # готовим данные для записи
            self.__prepare_data__()

            # записываем данные в файл
            bmp_file.write(self.bmp_header)
            bmp_file.write(self.bmp_info)
            bmp_file.write(self.img_array)



# параметры отображения
bmp_dim = 1000
bmp_name = 'result_img'

try:
    bwr = BmpWriter(bmp_name, bmp_dim)
    bwr.save_file()
except Exception as ex:
    print(type(ex))
    print(ex)

