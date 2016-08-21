import sys

with open(sys.argv[1], 'r') as f:
   allInput = f.read()

lines = allInput.split('\n')

for i in xrange(1, int(lines[0])+1):
   num = int(lines[i])
   step = num
   if num == 0:
      print 'Case #{}: INSOMNIA'.format(i)
   else:
      digits = set([c for c in str(num)])
      while len(digits) < 10:
         num += step
         digits = digits | set([c for c in str(num)])
      print 'Case #{}: {}'.format(i, num)
