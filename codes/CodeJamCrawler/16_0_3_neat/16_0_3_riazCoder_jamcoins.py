def getNum(num,base):
    out = 0
    b = 1
    for i in num:
        if i == '1':
           out = out + b
        b = base*b
    return out

def is_prime(n):
  if n == 2 or n == 3: return True,0
  if n < 2 or n%2 == 0: return False,2
  if n < 9: return True,0
  if n%3 == 0: return False,3
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False,f
    if n%(f+2) == 0: return False,f+2
    f +=6
  return True,0 

def legit(x):
    ans = []
    for i in x:
        a,b = is_prime(i)
        if a == True:
            return []
        else:
            ans.append(b)
    return ans       

T = input()
for i in range(1,T+1):
    a,b = map(int,raw_input().split(' '))
    #print all the numbers between 1
    count = 0
    print "Case #{0}:".format(i)
    for i in range(2**(a-2)):
        if count == b:
            break
        x = []
        prime = False
        s = "1" + "{0:b}".format(i).zfill(a-2) + "1"
        #print s
        for i in range(2,11): #bases
            num = getNum(s[::-1],i)
            if is_prime(num)[0] == True:
                prime = True
                break
            x.append(num)
        if prime != True :
            #print x # jam coin rep in every base
            ret = legit(x)
            if len(ret) > 0:
                print s," ",
                for i in ret:
                    print i,
                print 
                count += 1
        
            
        
            
