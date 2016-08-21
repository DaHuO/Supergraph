import string
digs = string.digits + string.letters

def int2base(x, base):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

def factor(N):
  n=2
  while(n<200):
    if(N%n==0):
      return n
    else : n=n+1
  return 0
    
    
total=0

p=0
for num in range(65535,32768,-2):

    found=1
    fac=''
    nbase2=int2base(num,2)

    for ba in range(2,11):
        x= int(nbase2,ba)
        
        ret=factor(x)
        if ret==0:
            found=0
            break
        else:
            fac=fac+' '+str(ret)
    if found!=0:
      p=p+1
      print nbase2,fac
      if(p==50):
        break


