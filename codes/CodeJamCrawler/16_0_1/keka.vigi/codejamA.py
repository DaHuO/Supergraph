for case in range(1, int(input())+1):
     SLP = set()
     N   = int(input())
     t   = N
     if N==0:
          print('Case #{}: INSOMNIA'.format(case))
     else:
          while len(SLP)<10:
               temp = set(str(N))
               if set(str(N)) not in SLP:
                    SLP.update(temp)
               N   += t
          print('Case #{}: {}'.format(case,N-t))
