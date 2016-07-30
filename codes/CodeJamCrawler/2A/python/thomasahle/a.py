import sys
read = lambda t=int: list(map(t,sys.stdin.readline().split()))
array = lambda *ds: [array(*ds[1:]) for _ in range(ds[0])] if ds else 0

P, R, S = range(3)

def solve(n, top):
   if n == 0:
      return "PRS"[top]
   a = solve(n-1, top)
   b = solve(n-1, (top+1)%3)
   return min(a+b, b+a)

T, = read()
for testCase in range(T):
   n, rcnt, pcnt, scnt = read()
   ss = [solve(n,top) for top in (P,R,S)]
   #print(ss)
   ss = [s for s in ss
         if s.count('R')==rcnt and s.count('P')==pcnt and s.count('S')==scnt]
   if not ss:
      res = "IMPOSSIBLE"
   else:
      res = min(ss)
   print('Case #{}: {}'.format(testCase+1, res))

