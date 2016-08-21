fhand=open('D-small-attempt0.in','r')
x=int(fhand.readline())
caseNo=x+1
def lol (hilary,trump,otherGuy):
 up=hilary**trump
 down=up/hilary
 president=down*2
 list=[]
 while president<=up:
  list.append(president)
  president+=down
 fhand2.write(' '+str(2))
 print 2, 
 for num in list:
  fhand2.write(' '+str(num))
  print num,
 return list
fhand2=open('outputtt.txt','w')
for y in xrange(1,caseNo):
 itor=fhand.readline().rstrip().split(' ')
 fhand2.write ('Case #%d:' %(y))
 print 'Case #%d:' %(y),
 k=int(itor[0])
 c=int(itor[1])
 s=int(itor[2])
 try:
  if k**c==s:
   for num in xrange(s):
    fhand2.write(' '+str(num+1))
    print num+1,
  elif k==1:
   fhand2.write(' '+str(1))
   print 1
  elif s<k:
   fhand2.write(' IMPOSSIBLE')
   print 'IMPOSSIBLE',
  else:
   lol(k,c,s)
 except:
  print 'IMPOSSIBLE'
 print 
 fhand2.write('\n',)