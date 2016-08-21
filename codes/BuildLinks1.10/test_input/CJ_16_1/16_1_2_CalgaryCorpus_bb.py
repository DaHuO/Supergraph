import sys
import collections

def solve(num):
#   print "-"*10, num
   todos = []
   for l in xrange(0,2*num-1):
       linea = [int(w) for w in sys.stdin.readline().split()]
#       print linea
       for l in linea:
           todos.append( l )
   
   todos = sorted(todos)

   # todo esta repetido un nro par de veces, excepto algunos que no
   counter = collections.Counter(todos)
 
   answer = []
   for i in xrange(len(counter.values())):
      if counter.values()[i] % 2 == 1:
         answer.append(counter.keys()[i])

   answerstr = [str(x) for x in sorted(answer)]
 
   return answerstr
 
# main()
 
# read 1 number, use it to control the loop
for tc in xrange(1, int(sys.stdin.readline())+1):
    # read 2 numbers
    num = int(sys.stdin.readline().strip())
    # read several floats, keep the result in a list
 
    best = " ".join(solve(num))
    print 'Case #%d: %s' % (tc, best)
