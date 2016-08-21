import itertools
def stgen(st):
  dic = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"] 

 # st = '123' 

  output = '' 
  for i in st:
    #print i 
    output += dic[i] 
  return (sorted(output))

f = open('A-small-attempt0.in','r')
k = int(f.readline())

for case in range(k):

  inputSt = f.readline()[:-1] 
#  print inputSt
  lenmin = max(len(inputSt)/5-1,0) 
  lenmax = len(inputSt)/3+1 
  for i in range(lenmin, lenmax+1,1):
    for x in itertools.combinations_with_replacement(xrange(10), i):
      if sorted(inputSt) == stgen(x):
        print 'Case #'+str(case+1)+':',
        ou = '' 
        for i in range(len(x)):
          ou += str(x[i])
        print ou
        break

