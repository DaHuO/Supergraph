import sys
savein = sys.stdin
saveout = sys.stdout

fin = open('B-large.in','r')
fout = open('B-large.out','w')

sys.stdin = fin
sys.stdout = fout

def time(str,char1,char2):
    i = len(str)-1
    if i == -1:
        return 0
    if str[i] == char1:
        return time(str[0:i],char1,char2)
    elif str[i] == char2:
        str1 = str[:i]
        return time(str1,char2,char1) + 1

t = int(input())

for x in range(0,t):
    str = input()
    n = time(str,'+','-')
    print("Case #{0}: {1}".format(x+1, n))

sys.stdin = savein
sys.stdou = saveout
fin.close()
fout.close()
