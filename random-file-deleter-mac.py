import os
import random

count = 0
while (count < 1):
     _files = os.listdir('.')
     number = random.randint(0, len(_files) - 1)
     file_ = _files[number]
     count = count + 1
     os.remove(file_)
     print(f"Removed {file_}")
