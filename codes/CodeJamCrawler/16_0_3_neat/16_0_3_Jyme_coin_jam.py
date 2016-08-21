from math import sqrt
import itertools

count = 0
case = 1
target = open('out', 'w')

def is_prime(a):
  #print ">"+str(a)
  for number in itertools.islice(itertools.count(2), 1000000):
    
    #if a%number == 0:
      #print number
    if not a%number:
      return number
  return 0
      
    

with open('input') as f:
  next(f)
  for line in f:
    line = line.split(' ')
        
    N = int(line[0])
    J = int(line[1])
    
    output =  "Case #"+str(case)+":"
    print output
    target.write(output)
    target.write("\n")
    i = 0
    while True:
      
      li = list()
      coin = '1'+ str("{0:b}".format(i)).zfill(N-2) + '1'
      #print coin
      for k in range(2,11):
        div = is_prime(int(coin,k))
        if div == 0:
          li = []
          break
        else:
          li.append(div)
      if li != []:
        output = coin +' ' + ' '.join(map(str, li))
        print output
        count += 1
        target.write(output)
        target.write("\n")
      if count == J:
        break
      i += 1
      
    
    

    case += 1
    
target.close()

