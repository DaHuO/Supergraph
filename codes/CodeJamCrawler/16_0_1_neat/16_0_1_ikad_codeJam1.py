def getRes(s):
 if s=='0':
  return "INSOMNIA"
 a= []
 for i in range (10):
  a.append(False)
 i=2
 while True:
  z="".join(set(s))
  z=z.strip('\n')
  for char in s:
   a[int(char)]=True
  res = True
  for j in range (10):
   res=res and a[j]
  if res:
   return s
  s=str(int(s)/(i-1)*i)
  i+=1
  
f = open("C:\Users\ikad\Desktop\in.txt","r")
out = open("C:\Users\ikad\Desktop\out1.txt","w")
i=0
for line in f:
 if i == 0:
  tc=line
  i+=1
  continue
 print "line : "+line
 out.write("Case #"+str(i)+": "+getRes(line.strip('\n'))+"\n")
 i+=1
f.close()
out.close()
