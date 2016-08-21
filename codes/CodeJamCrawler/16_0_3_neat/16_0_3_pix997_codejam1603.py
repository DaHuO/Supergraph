p = [2,3,5,7]
def primefind(n):
  i = 9
  while i<n:
    f = 0
    for j in p:
      if i%j==0:
        f = 1
        break
      if j**2>i:
        break
    if f==0:
      p.append(i)
    i+=2
primefind(10**6)
def is_prime(n):
  f = 0
  for j in p:
    if n%j==0:
      f = 1
      break
    if j**2>n:
      break
  if f==0:
    return True
  else:
    return False
aa = [i for i in range(2**15,2**16)]
aa = filter(lambda x:x%2==1,aa)
aa = filter(lambda x:not is_prime(x),aa)
b = aa[:500]
def checkbase(n):
    a = bin(n)
    a = a[2:]
    f = 0
    for i in range(3,11):
        x = int(a,i)
        if is_prime(x):
            f=1
    if f==0:
        return True
    else:
        return False
def finddiv(n):
    a = bin(n)
    a = a[2:]
    for i in range(2,11):
        x = int(a,i)
        for j in p:
            if x%j==0:
                if j!=None:
                  print j,
                  break
    print ''
b = filter(lambda x:checkbase(x),b)
print "Case #1:"
for i in range(50):
    a = bin(b[i])
    a = a[2:]
    print a,
    finddiv(b[i])

    
