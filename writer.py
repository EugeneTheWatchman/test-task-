# -*- coding: utf-8 -*-

import os
# задаем путь нашего именного канала
FIFO_NAME = 'tmp\test_pipe'
# пробуем создать канал
try:
    os.mkfifo(FIFO_NAME)
except FileExistsError:
    # если он уже существует, то ОК (наверное)
    pass


text = input('Ваш текст:')  # вводите текст
while len(text) > 0:  # если он не пустой, то
    f = open(FIFO_NAME, 'w')  # открывается именнованный канал на запись
    f.write(text)  # записывается текст
    f.close()  # канал (на запись) закрывается
    text = input('Ваш текст: ')

os.unlink(FIFO_NAME)  # именной канал удаляется