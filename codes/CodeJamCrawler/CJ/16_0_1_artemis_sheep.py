t = int(raw_input())
x=1

mylist=[];

def deva(test) :
    while test!=0 :
          a=test%10
          test=test/10
          if standard == [] :
             return
          elif a in standard :
               standard.remove(a)
    return

def comp(test,x) :
    i=1
    while standard != [] : 
          deva(i*test)
          i+=1
    mylist.append('Case #'+str(x)+': '+str((i-1)*test))
    return

while t>0 :
      test = int(raw_input())
      if test!=0 :
          standard=[0,1,2,3,4,5,6,7,8,9];
          comp(test,x)
      else :
           mylist.append('Case #'+str(x)+': INSOMNIA')
      x+=1
      t-=1

for p in mylist :
    print p
