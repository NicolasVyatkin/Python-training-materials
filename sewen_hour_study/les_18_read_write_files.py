import os

# 'r' открыйть для чтения (ао умолчанию)
# 't' открыть в ткстовом режиме (по умолчанию)
# 'w' открыть для записи, содержимое файла, если файла нет, создаёт новый
# 'a' открыть для дозаписи в конец файла, если файла нет, создаёт новый
# 'b' открыть в бинарном режиме
# '+' открыть для чтения и записи 'r+', 'w+', 'a+'
#########################################################################
"""Загрузка в файл информации из каталога"""
# list_paths = []
# for adr, folder, file in os.walk('D:\\Флэшка(перебрать)\DCIM'):
#     for i in file:
#         full_path = os.path.join(adr, i)
#         list_paths.append(full_path)
#
# r = open('text.txt', 'w', encoding='utf-8') # кодировка файла utf-8, его считывание будет возможно только при указании этой кодировки
# for x in list_paths:
#     r.write(x + '\n')
# r.close()
#########################################################################
# r.write('Some text')
# r.close()
# r = open('text.txt')
# u = r.read()
# print(u)
# r.close()
###############################################################################
"""Чтение из файла"""
# r = open('text.txt', encoding='utf-8')
# for i in r:
#     if '5938.JPG' in i:
#         print(i)
# r.close()
###############################################################################
"""Побитовое копирование файла"""
r = open('text.txt', 'rb')
y= open('Копия text.txt','wb')
while True:
    var=r.read(1024*1024)#ограничение копирования в 1 мб
    print(var.__sizeof__()) #показывает сколько места занимает файл в оперативной памяти
    if var.__sizeof__()==33:
        break
    y.write(var)
print('end of code')

r.close()
y.colose()
