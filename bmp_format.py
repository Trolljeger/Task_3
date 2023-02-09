'''
Описание формата BMP файла
'''


F_FORMAT_STR = '='        # выравнивание                            0 байт, не учитывается в заголовке

# форматная строка заголовка файла BMP
F_TYPE_STR = 'H'                # тип файла "BM"                          2 байта
F_SIZE_STR = 'I'                # размер файла в байтах                   4 байта
F_RESERVED1_STR = 'H'           # резерв                                  2 байта
F_RESERVED2_STR = 'H'           # резерв                                  2 байта
F_OFFSET_BITS_STR = 'I'         # Смещение изображения от начала файла    4 байта
# Общий размер заголовка файла 14 байт


# Форматная строка заголовка файла BMP
BMP_FILE_HDR_STR = F_FORMAT_STR + F_TYPE_STR + F_SIZE_STR + F_RESERVED1_STR + F_RESERVED2_STR + F_OFFSET_BITS_STR


# форматная строка информационного заголовка BMP
I_SIZE_STR = 'I'                # Длина заголовка 40 байт                   4 байта
I_WIDTH_STR = 'I'               # Ширина изображения, точки                 4 байта
I_HEIGTH_STR = 'I'              # Высота изображения, точки                 4 байта
I_PLANES_STR = 'H'              # Число плоскостей                          2 байта
I_BITCOUNT_STR = 'H'            # Глубина цвета, бит на точку               2 байта
I_COMPRESSION_STR = 'I'         # Тип компрессии (0 - несжатое изображение) 4 байта
I_SIZEIMAGE_STR = 'I'           # Размер изображения, байт                  4 байта
I_XPELSPERMETER_STR = 'I'       # Горизонтальное разрешение, точки на метр  4 байта
I_YPELSPERMETER_STR = 'I'       # Вертикальное разрешение, точки на метр    4 байта
I_COLORSUSED_STR = 'I'          # Число используемых цветов                 4 байта
I_COLORSIMPORTANT_STR = 'I'     # Число основных цветов                     4 байта
# Общий размер информационного заголовка файла 40 байт

BMP_INFO_HDR_STR = F_FORMAT_STR + I_SIZE_STR + I_WIDTH_STR + I_HEIGTH_STR + I_PLANES_STR + I_BITCOUNT_STR + I_COMPRESSION_STR + I_SIZEIMAGE_STR + I_XPELSPERMETER_STR+ I_YPELSPERMETER_STR + I_COLORSUSED_STR + I_COLORSIMPORTANT_STR

# форматная строка таблицы цветов
#BMP_COLOR_TABLE_STR = '256I'    # 256 элементов по 4 байта                  1024 байта

