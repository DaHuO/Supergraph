file=open('B-large.in','r')
import sys
sys.setrecursionlimit(1800000)

#file=open('test.txt','r')
file1=open('output-b.txt','w')

# 011010110000
# 01110
# 10001

for j in range(1,int(file.readline())+1):
    pans = (file.readline())
    #print(pans)
    pancakes=[]
    for i in pans:
        #print(i+'+',end='')
        if i=='-':pancakes.append(False)
        elif i=="+": pancakes.append(True)
    lowest=0
    for a in range(len(pancakes)):
        if not pancakes[-1]:
            lowest+=1
            for b in range(len(pancakes)-1):
                pancakes[b] = not pancakes[b]
        pancakes=pancakes[:-1]
    print("Case #%d: %d" % (j,lowest))
    file1.write("Case #%d: %d\n" % (j,lowest))
    #print('\n\n\n')

file.close()
file1.close()

