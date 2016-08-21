
def main():
   T = int(raw_input())
   for c in range(1, T+1):
      K, C, S = [int(val) for val in raw_input().split(" ")]
      if K!=S:
         print "Case #"+str(c)+": IMPOSSIBLE"
      else:
         tilesToClean = []
         kpowc1 = pow(K,C-1)
         for j in range(1, K+1):
            if C>1:
               tilesToClean.append(kpowc1*(j-1)+j)
            else:
               tilesToClean.append(j)
         print "Case #"+str(c)+":"," ".join(str(x) for x in tilesToClean)
main()