f=open("A-large.in","r")
g=open("phone.out","w")

T = int(f.readline())
digits = [['Z','ZERO',0],['W','TWO',2],['X','SIX',6],['G','EIGHT',8],['S','SEVEN',7],['V','FIVE',5],['I','NINE',9],['F','FOUR',4],['O','ONE',1],['E','THREE',3]]

def strtolist(s):
  L = [x for x in s]
  return L

def listtostr(L):
  s = ''
  for x in L:
    s = s+str(x)
  return s

for i in range(0,T):

  s = f.readline()[:-1]
  L = strtolist(s)
  k = 0
  numbers = []
  while len(L) > 0:
    if digits[k][0] in L:
      for ch in digits[k][1]:
        L.remove(ch)
      numbers.append(digits[k][2])
    else:
      k+=1
  numbers.sort()
  ans = listtostr(numbers)

  g.write("Case #"+str(i+1)+": "+ans+"\n")

  
  
  
