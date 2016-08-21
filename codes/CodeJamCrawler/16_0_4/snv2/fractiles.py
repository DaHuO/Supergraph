__author__ = 'snv'
f = open('D-small-attempt0.in','r')
g = open('output.txt', 'w')

n = int(f.readline())
for j in range(n):
     k,c,s = (int(m) for m in f.readline().strip().split())
     step = k**(c-1)
     print('Case #{0}: {1}'.format(j," ".join(str(m*step+1) for m in range(s))))
     g.write('Case #{0}: {1}\n'.format(j+1," ".join(str(m*step+1) for m in range(s))))
f.close()
g.close()



