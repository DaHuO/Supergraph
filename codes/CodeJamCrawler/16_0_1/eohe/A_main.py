

def solution(N):
  temp = int(N[0])
  
  digits = list(str(temp))
  digits = set(digits)
  count = 2
  
  while count<=100:
    new = temp*count
    digits = digits.union(list(str(new)))
    #print digits

    if len(set(digits)) == 10:
      return str(new)
    else:
      count+=1
  
  #print digits
  return 'INSOMNIA' 
    


if __name__=="__main__":
  
  #in_file = "A-small-attempt0.in"
  in_file = 'A-large.in'
  out_file = 'A_output.out'

  f = open(in_file, 'r')
  o = open(out_file, 'w')
  
  num_cases = int(f.readline().strip())
  
  for case in range(1, num_cases+1):
   
    N = f.readline().split()
    
    result = solution(N)
    
    
    res = "Case #" + str(case) + ": " + str(result)
    print str(res)   
    o.write( res + ' \n')
    
  f.close()
  o.close()