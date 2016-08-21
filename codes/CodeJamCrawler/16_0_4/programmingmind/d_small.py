import sys

with open(sys.argv[1], 'r') as f:
   allInput = f.read()

lines = allInput.split('\n')

def findNdx(K, C, pos):
   # total length will be K**C
   # each letter expands to K letters each step
   # so each letter is responsible for K**(C-1) letters

   return 1 + (pos - 1) * K**(C-1)

for i in xrange(1, int(lines[0])+1):
   parts = lines[i].split()
   K = int(parts[0])
   C = int(parts[1])
   S = int(parts[2])

   print 'Case #{}: {}'.format(i, ' '.join([str(findNdx(K, C, p+1)) for p in xrange(K)]))
