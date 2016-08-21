
def solution(a):
  a=a + '+'
  t=0
  for i in range(len(a)-1):
    if a[i]!=a[i+1]:
      t=t+1
  return t

T=int(raw_input())

for i in range(1,T+1):
  S=raw_input()
  print('Case #%d: %d' % (i,solution(S)))
