f = open('input', 'r');
N = int(f.readline())

def fun(test, s):
 for x in str(s):
  test[int(x)]=1;
 return test

for i in range(N):
 s = int(f.readline())
 test = [0 for k in range(10)]
 b = True
 for j in range(1,1000000):
  test = fun(test, s*j)
  if sum(test) == 10:
   print 'Case #%d: %d' %(i+1, j*s)
   b = False
   break
 if b: print 'Case #%d: INSOMNIA' %(i+1)
