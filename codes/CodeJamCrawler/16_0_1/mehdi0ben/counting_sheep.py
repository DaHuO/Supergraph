output = open("A-large-.out","w")
with open("A-large.in") as f:
    T = f.readline()
    T = int(T)
    for i in range (0, T):
        N = f.readline()
        N = int(N)
        if(N == 0) :
          output.write("Case #"+str(i+1)+": INSOMNIA \n")
        else :
           case = [None]*10
           for k in range(0,10) : case[k] = False
           j = 1;
           while any(case[k] == False for k in range(0, 10)): 
                M = N * j
                split = [int(w) for w in str(M)]
                for a in split :
                  case[a] = True
                j = j + 1
           output.write("Case #"+str(i+1)+": "+str(M)+"\n")

