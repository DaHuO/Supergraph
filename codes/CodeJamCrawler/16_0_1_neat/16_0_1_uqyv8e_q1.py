def func(n):
   if n == 0:
       return 'INSOMNIA'
   i = 1
   r = set()
   while True:
       for c in str(n * i):
           r.add(c)
           if len(r) == 10:
               return n * i
       i += 1

T = int(input())
for i in range(T):
    N = int(input())
    print('Case #{}: {}'.format(i+1, func(N)))
