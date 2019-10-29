import os
import random

_files = os.listdir('.')
number = random.randint(0, len(_files) - 1)
file_ = _files[number]
count = 0
while (count < 10):
    count = count + 1
    os.remove(file_)
