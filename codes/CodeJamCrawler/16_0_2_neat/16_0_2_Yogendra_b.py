#CodeJam16 Qualifier b.py
def getResArr(inp):
 a = ''
 for i in inp:
  a=a+'+'
 return a

def checkFlip(inp):
 res = inp
 count = 0
 const = ['-','+']
 resAr = getResArr(inp)
 while res != resAr:
  count +=1
  const = ['-','+']
  const.remove(res[0])
  tmp = ''
  flag = 0
  reset = 1
  for i in res:
	if reset == 1:
		tmp=tmp+const[0]
		reset = 0
		continue
	if tmp[0] == i:
		flag = 1
	if flag == 1:
	 tmp = tmp+i
	if flag == 0: 
	 tmp=tmp+const[0]
  res = tmp
 return count 

lines = input()
count = 0
for i in range(lines):
 count+=1
 inp = raw_input()
 if inp == '+' :
  print 'Case #'+str(count)+': 0'
 else:
  res = checkFlip(inp)
  print 'Case #'+str(count)+': '+str(res)