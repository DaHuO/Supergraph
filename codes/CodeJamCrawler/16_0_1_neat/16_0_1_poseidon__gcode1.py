i=int(raw_input())
for x in range(i):
  a=raw_input()
  n=0
  for q in range(len(a)):
  	n=n*10+int(a[q])
  p=1
  s=0
  i=1
  count=0
  d=dict()
  for y in range(10):
     d[y]=0
  if n==0:
    print "Case #" + str(x+1) + ":" + " INSOMNIA"
  else:
    while True:
      s=n*p
      v=str(s)
      for z in v:
        d[int(z)]+=1
      for z in range(10):
        if d[z]>0:
           count+=1
      if count ==10:
        break
      count=0
      p+=1
    print "Case #" + str(x+1) + ":" + " " + str(s)