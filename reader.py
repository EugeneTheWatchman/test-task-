# -*- coding: utf-8 -*-
from num2str import *

FIFO_NAME = 'tmp\test_pipe'  # задается имя именного канала

while True:
    f = open(FIFO_NAME, 'r')  # канал открывается для чтения
    text = f.read()  # читаются символы
    print(num_to_text(text))  # воводятся на экран
    f.close()  # канал закрывается для чтения