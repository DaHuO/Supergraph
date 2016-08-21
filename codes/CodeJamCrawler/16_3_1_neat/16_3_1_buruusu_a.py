from heapq import *

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solve(n, p):
  freq = list(list(pair) for pair in zip((-n for n in p), ALPHABET))
  heapify(freq)
  # print(freq)
  head = freq[0]
  soln = []
  while head[0] < 0 and not(len(freq) == 2 and head[0] == -1):
    #print(freq)
    n = -sum(i[0] for i in freq)
    #print('n', n)
    #print(freq)
    if -head[0] < -1 and -head[0] > n/2:
      #print(soln)
      raise Exception('no!')
    soln.append(head[1])
    f = head[0]
    head[0] += 1
    heapify(freq)
    head = freq[0]
    freq = [i for i in freq if i[0] < 0]
    if head[0] == f and (len(freq) > 2 or head[0] < -1):
      soln[-1] += head[1]
      head[0] += 1
      heapify(freq)
      head = freq[0]
      freq = [i for i in freq if i[0] < 0]
    #print(soln[-1])
  # Final two at the same time
  if freq:
    soln.append(freq[0][1] + freq[1][1])
  return ' '.join(soln)

t = int(input())
for i in range(1, t + 1):
  n = int(input())
  p = [int(i) for i in input().split()]
  print("Case #%d: %s" % (i, solve(n, p)))
