cases = int(input())

for line in range(1,cases+1):
      n=int(input())
      ds=[]
      m=0
      while n!=0 and len(ds)<10:
            m+=1
            for char in str(n*m):
                  if char not in ds:
                        ds.append(char)
      if len(ds)==10:
            print("Case #"+str(line)+": "+str(n*m))
      else:
            print("Case #"+str(line)+": INSOMNIA")
            
