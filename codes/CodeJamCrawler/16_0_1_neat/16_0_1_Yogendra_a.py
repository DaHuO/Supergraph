#CodeJam16 Qualifier a.py
def checkN(num,allN):
 sN = str(num)
 for s in sN:
  if int(s) in allN:
	allN.remove(int(s))
 return allN

def checkSleep(num):
 oriNum = num
 allN = [0,1,2,3,4,5,6,7,8,9]
 allN = checkN(num,allN)
 while allN != []:
	num = num+oriNum
	allN = checkN(num,allN)
 return num
 
lines = input()
count = 0
for i in range(lines):
 count+=1
 inp = input()
 if inp == 0 :
  print 'Case #'+str(count)+': INSOMNIA'
 else:
  res = checkSleep(inp)
  print 'Case #'+str(count)+': '+str(res)