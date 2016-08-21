import sys
read = lambda t=int: list(map(t,sys.stdin.readline().split()))
array = lambda *ds: [array(*ds[1:]) for _ in range(ds[0])] if ds else 0

# i is the number of persons considered
def solve(i,k,s):
   global ps
   if s < 0 or s > i or i < k:
      res = 0
   elif k == 0:
      res = int(s == 0)
   else:
      skip = solve(i-1, k, s)
      yes = solve(i-1, k-1, s-1)
      no = solve(i-1, k-1, s)
      res = max(skip, ps[i-1]*yes + (1-ps[i-1])*no)
      print((i,k,s),skip, yes,no,'=', res)
   return res

def solve2(k,n):
   global ps
   res = 0
   for S in range(2**n):
      if bin(S).count('1') == k:
         x = 0
         T = S
         while T != 0:
            if bin(T).count('1') == k//2:
               y = 1
               for j in range(n):
                  if T & 1<<j:
                     y *= ps[j]
                  elif S & 1<<j:
                     y *= 1-ps[j]
               #print(bin(S), bin(T), y)
               x += y
            T = (T-1) & S
         res = max(res, x)
   return res

T, = read()
for testCase in range(T):
   N, K = read()
   ps = read(float)
   #dp = array(n,k,2*n+10)
   #for i in range(n):
   #   for k in range(K):
   #      for s in range(

   #res = dp[N-1][
   #dp[

   #for s in range(0,K+1):
   #   print(s, solve(N-1,K,s))

   #res = solve(N,K,K//2)
   res = solve2(K,N)


   print('Case #{}: {}'.format(testCase+1, res))

