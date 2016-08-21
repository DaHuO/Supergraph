
iput=[]
i=0
line=0
output=[]


def detectSleep(x,j):
  reference= set(['0','1','2','3','4','5','6','7','8','9'])
  toCheck=set([])
  i=1
  if x==0:
      return
  while(reference!=toCheck):
    temp=int(x)*i
    for y in str(temp):
        toCheck.add(y)
    i=i+1

  print "Case #"+str(j)+": "+str(temp)
with open('op.txt','r') as f:
    iput.append(f.read())

iput=iput[0].split("\n")
iput=iput[:len(iput)-1]
j=1
for x in iput[1:]:
    if (x=="0"):
      print "Case #" + str(j) + ": " + "INSOMNIA"
      j = j + 1
      continue
    detectSleep(x,j)
    j=j+1




