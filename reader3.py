# -*- coding: utf-8 -*-
from num2str import *
import time
import os

FIFO_NAME = 'tmp\test_pipe'  # задается имя именного канала

f = os.open(FIFO_NAME, os.O_RDONLY)  # канал открывается для чтения

while True:
    time.sleep(0.5)
    text = os.read(f,20).decode()  # читаются 20 символов
    if len(text) > 0:
        print(num_to_text(text))  # воводятся на экран

f.close()  # канал закрывается для чтения