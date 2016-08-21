def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())



_T = readint()
for _t in range(_T):
  done=0
  N = int(raw_input())
  final=0
  List = [0,0,0,0,0,0,0,0,0,0]
  if N is not 0:
    i=1
    while(done != 10):
      n=i*N
      final=n
      while(n!=0):
        x=n%10
        n=n/10
        List[x]=1 
      done=sum(List)
      i+=1
  if final is 0:
    final = "INSOMNIA"
  print 'Case #%i:'%(_t+1),final
