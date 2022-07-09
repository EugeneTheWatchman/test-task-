# -*- coding: utf-8 -*-
from num2str import *
import time

FIFO_NAME = 'tmp\test_pipe'  # задается имя именного канала

f = open(FIFO_NAME, 'r')  # канал открывается для чтения

while True:
    time.sleep(0.5)
    text = f.read()  # # читаются символы
    if text:
        print(num_to_text(text))  # воводятся на экран

f.close()  # канал закрывается для чтения