n = raw_input()
b = [0,1,2,3,4,5,6,7,8,9]
t = []
flag = 0
for i in range(int(n)):
  a=1
  s=[]
  r = raw_input()
  r = int(r)
  while(a<=10**6):
    s = list(set(s) | set([int(x) for x in str(r*a)]))
    s.sort()
    if (s==b):
      flag = 1
      break
    a+=1
  if(flag!=1):
    t.append("INSOMNIA")
  else:
    t.append(r*a)
for i in range(len(t)):  
  print("Case #" + str(i+1) + ": " + str(t[i]))
    
  
  