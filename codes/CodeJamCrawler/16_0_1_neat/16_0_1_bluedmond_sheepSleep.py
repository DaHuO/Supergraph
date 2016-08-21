fhand=open('A-large.in','r')
x=int(fhand.readline())
caseNo=x+1

def populate(num):
 digits=dict()
 keys='1234567890'
 stry=list(keys)
 for x in stry: 
  digits[x]=digits.get(x,0)+1
 
 sets=str(num)
 mul=1
 for z in sets:
  digits[z]=digits.get(z,0)+1
 while 1 in digits.values():
  mul+=1
  final=mul*num
  setts=str(final)
  for h in setts:
   digits[h]=digits.get(h,0)+1
  next
 return final

fhand2=open('outputtt.txt','w')
for y in xrange(1,caseNo):
 ithor=fhand.readline().rstrip()
 fhand2.write ('Case #%d: ' %(y))
 print 'Case #%d:' %(y),
 strng=int(ithor)
 if strng==0:
  print 'INSOMNIA'
  fhand2.write('INSOMNIA\n')
 else: 
  print populate(strng)
  fhand2.write(str(populate(strng))+ '\n')