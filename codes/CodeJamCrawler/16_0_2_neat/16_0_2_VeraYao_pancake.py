f = open('B-large.in','r') 
n = int(f.readline()) 

for k in range(n):
  pancake = f.readline() 
  num = 0
  flag = '+'
  for i in range(len(pancake)-1, -1, -1): 
    if flag != pancake[i] and pancake[i] in '+-':
      num += 1
      flag = pancake[i]
  print 'Case #'+str(k+1)+': '+str(num) 


