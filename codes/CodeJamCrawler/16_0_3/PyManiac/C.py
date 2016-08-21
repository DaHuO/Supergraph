import itertools

def isnotprime(n):
  z = int(n ** 0.5) + 1
  for x in itertools.count(3 ,2) :
    if x > int(n ** 0.1):
      break
    if (n % x) == 0:
      return x
  return True
  

def check(value):
  factors = []
  for i in range(2,11):
    val = int(value , i)
    fc = isnotprime(val)
    if fc == True :
      return False
    else:
      factors.append(fc)
  return factors



N = 32 - 2
K = 500

ans = ["Case #1:"]
for line in itertools.product('01', repeat = N):
  value = '1' +  ''.join(line) + '1'
  #print(value , len(ans))
  if len(ans) >  K  :
    break
  temp_ans = check(value)
  if temp_ans != False :  
    s = value + " "  + " ".join([str(j) for j in temp_ans] )
    ans.append(s)

fp = open('a.out' , 'w+')
fp.write('\n'.join(ans[:K+1]))
fp.close()


