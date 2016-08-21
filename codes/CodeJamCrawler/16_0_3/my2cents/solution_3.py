import random
for t in range(int(input())):       # First input is the number of cases.
    (N, J) = tuple(list(map(int, input().split())))
    
    Jdecimal = random.randint(0, 2**(N-2) - 1)
    Jbinary  = bin(Jdecimal)[2:]
    Jbinary  = '1' + Jbinary + '1'
    JList = [(Jbinary, [5])]

    def is_prime(n):
      if n == 2 or n == 3: return -1
      if n < 2 or n%2 == 0: return 2
      if n < 9: return -1
      if n%3 == 0: return 3
      r = int(n**0.5)
      f = 5
      while f <= r:
        if n%f == 0: return f
        if n%(f+2) == 0: return f+2
        f +=6
      return -1    
    
    for i in range(J+1):
        while(1):
            Jdecimal = random.randint(0, 2**(N-2) - 1)
            Jbinary  = bin(Jdecimal)[2:]
            #Jlen     = length(str(Jbinary))
            #Jgap     = N - 2 - Jlen
            Jbinary  = '1' + Jbinary.zfill(N-2) + '1'
            Jfactors = []
            for temp in JList:
                Jexists = False
                if temp[0] == Jbinary:
                    Jexists = True
                    break
            if not(Jexists):
                for base in range(9):
                    Jnum = int(Jbinary, base+2)
                    Jfact = is_prime(Jnum)
                    if Jfact == -1:
                        Jprime = True
                        break
                    else:
                        Jfactors.append(Jfact)
                if Jfact != -1:
                    JList.append((Jbinary, Jfactors))
                    break
                
                    
    print("Case #%d:"%(t+1))
    for i in range(J):
        print(JList[i+1][0], *JList[i+1][1], sep=' ')
        
