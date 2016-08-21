import re

def isAllHappy(panSet):
  return panSet==set(['+'])

def isAllSame(panSet):
  return len(panSet)==1

def solution(pstack):
  
  if pstack=='':
    return 0
  
  panSet = set(list(pstack))
  
  if isAllSame(panSet):
    if isAllHappy(panSet):
      return 0 #no need to flip
    return 1 #needs a flip
  
  flat_happy = re.sub("[+]+", '+', pstack)
  last_plus = flat_happy.rfind('+')
  
  #print flat_happy, last_plus
  
  if last_plus == 0:
    return solution(flat_happy[1:]) + 1
  else:
    return solution(flat_happy[:last_plus])+solution(flat_happy[last_plus:])


if __name__=="__main__":
  
  #in_file = "B-small-attempt0.in"
  in_file = 'B-large.in'
  out_file = 'B_output.out'

  f = open(in_file, 'r')
  o = open(out_file, 'w')
  
  num_cases = int(f.readline().strip())
  
  for case in range(1, num_cases+1):
   
    pstack = f.readline().split()[0]
    
    #pstack = '--+-'
    
    result = solution(pstack)
    
    
    res = "Case #" + str(case) + ": " + str(result)
    print str(res)   
    o.write( res + ' \n')
    
  f.close()
  o.close()