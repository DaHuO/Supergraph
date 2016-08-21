f = open('A-large.in','r') 
n =int(f.readline()) 

cases = [0 for i in range(n)] 
for i in range(n):
  cases[i] = int(f.readline()) 
for i in range(n):
  if cases[i] == 0: 
    print 'Case #'+str(i+1)+': INSOMNIA' 
    continue 
  appear  = [0  for l in range(10)] 
  sheep = cases[i] 
  num = 0 
  while sum(appear) != 10: 
    num += 1
    m = sheep*num 
    while m: 
      k = m%10
      appear[k] = appear[k]|1 
      m = m/10 
  print 'Case #'+str(i+1)+': '+str(num*sheep) 


