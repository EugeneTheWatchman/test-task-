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


text = input('Ваш текст: ')  # вводите текст
while len(text) > 0:  # если он не пустой, то
    f = os.open(FIFO_NAME, os.O_WRONLY)  # открывается именнованный канал на запись
    os.write(f,text.encode())  # записывается текст
    os.close(f)  # канал (на запись) закрывается
    text = input('Ваш текст: ')

#os.unlink(FIFO_NAME)  # именной канал удаляется