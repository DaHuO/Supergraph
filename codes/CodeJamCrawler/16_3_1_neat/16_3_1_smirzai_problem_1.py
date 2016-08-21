
import sys
from heapq import heappush, heappop

def solve(n, l):
   h = []

   result = []
   for i in range(len(l)):
      aa = (-l[i], chr(ord('A') + i))

      heappush(h, aa)
   s = sum(l)
   while h:
         a = heappop(h)


         if s > 1 and s != 3:
            if -a[0] > 1:
               heappush(h, (a[0] + 1, a[1]))
            b = heappop(h)
            if -b[0] > 1:
               heappush(h, (b[0] + 1, b[1]))
            s -= 2
            result.append(a[1] + b[1])
         else:
            result.append(a[1])
            s -= 1


   return result



if  len(sys.argv) == 2:
   filename = sys.argv[1]
else:
   filename = "sample"


f = open(filename + ".in", "r")
o = open(filename + ".out", "w")
n = f.readline()
n = int(n)


for i in range(n):
   line = f.readline().rstrip('\r\n')
   n = int(line)
   line = f.readline().rstrip('\r\n')
   tokens =  line.split(" ")
   l = map(int, tokens)
   l = list(l)
   result = solve(n, l)
   o.write("Case #" + str(i+1) + ": " + " ".join(result) + '\n');

o.close()
f.close()
