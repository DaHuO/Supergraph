_T = int(raw_input())
for _t in range(_T):
  complete=0
  res = 0
  stack = raw_input()


  while(len(stack)!=0):
    stacklist = list(stack)
    findex = stack.find('-')
    lindex = stack.rfind('-')
    if lindex == -1:
      break
      
    stacklist = stacklist[0:lindex+1]
    if len(stacklist)==0:
      break

    if findex >0:
      res+=1
      for i in xrange(0,findex):
        stacklist[i]='-'

    
    if lindex > -1:      
      res+=1

      stacklist.reverse()

      for x in xrange(0,len(stacklist)):
        if stacklist[x] is '-':
          stacklist[x] = '+'
        else:
          stacklist[x] = '-'

    stack=''.join(stacklist)
  
  print 'Case #%i:'%(_t+1),res
