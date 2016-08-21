import sys

input = sys.stdin

def solve(lists):
  out = []
  for i in range(N):
    lists.sort()
    heads = [l[0] for l in lists]
    if len(lists)<2:
      out.append(lists[0][0])
    elif lists[0][0] !=lists[1][0]:
      if lists[0][0] < lists[1][0]:
        hd = lists[0]
      else:
        hd = lists[1]
      for n in hd[1:]:
        heads.remove(n)
      heads.sort()
      for n in heads:
      	out.append(n)
      s = str(out[0])
      for n in out[1:]:
        s+= ' '+str(n)
      return s
    else:  
      top = lists[0] + lists[1] 
      heads.sort()
      top.sort()
      j = 0
      while j<len(heads) and heads[j] == top[j]:
        j+=1
      out.append(top[j])
    lists = [ls[1:] for ls in lists[2:]]
  s = str(out[0])
  for n in out[1:]:
    s+= ' '+str(n)
  return s

for case in range(int(input.readline())):
  N = int(input.readline())
  lists = []
  for i in range(2*N-1):
    ls = input.readline().split()
    lists.append([int(s) for s in ls])
  print("Case #"+ str(case+1) +":", solve(lists))
  
