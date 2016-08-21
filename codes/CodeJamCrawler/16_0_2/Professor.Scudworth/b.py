import sys

round_count = int(sys.stdin.readline())
for i in range(round_count):
    flip_count = 0
    cakes = sys.stdin.readline().strip()
    for j in range(len(cakes)-1):
        if cakes[j] != cakes[j+1]:
            flip_count += 1
    if cakes[len(cakes)-1] == '-':
        flip_count+=1
    print("Case #",i+1,": ",flip_count,sep='')
