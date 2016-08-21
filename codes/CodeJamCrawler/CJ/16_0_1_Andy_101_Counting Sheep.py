def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

T=input()
for ii in range(0,T):
    n=input()
    k=n
    l=list()
    j=1
    nn=""
    if(n==0):
        print "Case #%d: INSOMNIA"%(ii+1)
    else:
        while nn != "0123456789":
            for i in range(0,len(str(n))):
                l.append(int(str(n)[i]))
            nn=""
            l.sort()
            l=uniq(l)
            for i in range(0,len(l)):
                nn=nn+str(l[i])
            if nn == "0123456789":
                print "Case #%d: %d"%(ii+1,n)
            n=k
            j=j+1
            n=n*j
            

            
