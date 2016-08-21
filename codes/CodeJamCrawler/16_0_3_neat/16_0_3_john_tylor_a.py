def is_prime(n):
  if n == 2 or n == 3: return True,0
  if n < 2: return False,1
  if n%2 == 0: return False,2
  if n < 9: return True,0
  if n%3 == 0: return False,3
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False,f
    if n%(f+2) == 0: return False,(f+2)
    f +=6
  return True,0   





t=int(raw_input())
for ist in range(t):
    l=list(map(int, raw_input().split()))
    print "Case #"+str(ist+1)+":"
    count,num1=0,-1   
    while True:
        num1=num1+1
        a='1'+("{0:b}".format(num1)).zfill(l[0]-2)+'1'
        if count==l[1]:
            break
        k=9
        az=[]
        aa,kk = is_prime(int(a))
        if kk!=0:
            az.append(kk)
        else:
            continue       
        while aa==False and k>1:
            aa,kk = is_prime(int(a,k))
            if kk!=0:
                az.append(kk)
                k=k-1
            else:
                break    
        if k==1:
            print a,
            for iss in range(0,9):
                print az[8-iss],
            count=count+1
            print '\n'
            
