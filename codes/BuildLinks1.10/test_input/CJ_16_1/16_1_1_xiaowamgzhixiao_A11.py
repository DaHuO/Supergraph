
import sys
savein = sys.stdin
saveout = sys.stdout

fin = open('A-large.in','r')
fout = open('A-large.out','w')

sys.stdin = fin
sys.stdout = fout


t = int(input())
for x in range(0,t):
    s = str(input())
    a = []
    for y in s:
        if len(a) == 0:
            a.append(y)
        else:
            if y >= a[0]:
                a.insert(0,y)
            else:
                a.append(y)
    print("Case #{0}:".format(x + 1), end=" ")
    for y in a:
        print(y, end="")
    print("")



sys.stdin = savein
sys.stdou = saveout
fin.close()
fout.close()
