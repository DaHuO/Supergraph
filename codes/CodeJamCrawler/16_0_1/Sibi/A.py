import sys

iFile = open(sys.argv[1],"r")

T = int(iFile.readline().strip())

for t in range(T):
    line = iFile.readline().strip()
    
    number = int(line)
    
    if number == 0:
      answer = 'INSOMNIA'
    else:  
      lastNumber = 0
      i = 1
      digits = [0]*10
      
      while(True):
        lastNumber = i * number
        for d in str(lastNumber):
          digits[int(d)] = 1
        
        i += 1
        
        if sum(digits) == 10:
          break
          
      answer = lastNumber
    output = str(answer)
    
    print("Case #"+str(t+1)+": "+output)
