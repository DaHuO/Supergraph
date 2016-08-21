import re
def count(pancakes):
    origin = pancakes[0]
    cnt = 0
    for i in pancakes:
        if origin != i:
            cnt += 1
        origin = i

    if pancakes[-1] == "+":
        return cnt
    else:
        return cnt + 1

# print count("--+-")

f = open("B-large.in","r+")
w = open("output","w+")
f.readline()
idx = 0
for row in f.readlines():
    idx += 1
    result = count(re.sub('\s','',row))
    w.write("Case #"+str(idx)+": "+str(result)+"\n")