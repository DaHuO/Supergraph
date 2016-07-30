import time
import random
import numpy as np
f = open('text.txt', 'r')
list = f.read()
f.close()
list = list.split(',')
list = np.array(list, np.int16).tolist()
count = 0
start = time.time()
changed = True
while changed:
    changed = False
    count = count + 1
    for i in range(1, len(list)):

        if list[i-1] > list[i]:
            changed = True
            list[i-1],list[i] = list[i], list[i-1]

print list
print (time.time()-start)
