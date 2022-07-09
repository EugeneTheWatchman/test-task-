# -*- coding: utf-8 -*-

# такой подход не работает, т.к. нужно закрывать файл
# по окончанию записи, чтобы в канал информация ушла

import os
# задаем путь нашего именного канала
FIFO_NAME = 'tmp\test_pipe'
# пробуем создать канал
try:
    os.mkfifo(FIFO_NAME)
except FileExistsError:
    # если он уже существует, то ОК (наверное)
    pass


f = os.open(FIFO_NAME, os.O_WRONLY)  # открывается именнованный канал на запись

text = input('Ваш текст: ')  # вводите текст
while len(text) > 0:  # если он не пустой, то

    os.write(f,text.encode())  # записывается текст
    text = input('Ваш текст: ')

os.close(f)  # канал закрывается
os.unlink(FIFO_NAME)  # именной канал удаляется