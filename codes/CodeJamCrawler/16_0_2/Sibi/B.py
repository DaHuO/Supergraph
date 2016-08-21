import sys

iFile = open(sys.argv[1],"r")

T = int(iFile.readline().strip())

for t in range(T):
    line = iFile.readline().strip()
    line = list(line)
    
    answer = 0
    
    while True:
      #print line
      if line[-1] == '+':
        for i in range(len(line)):
          if line[-i-1] != '+':
            line = line[:-i]
            break
        else:
          line = ''
      #print line
      if len(line) == 0:
        break
        
      answer += 1
      
      if line[0] == '+':
        for i in range(len(line)):
          if line[i] == '+':
            line[i] = '-'
          else:
            break
        
      else:
        line = ['+' if x == '-' else '-' for x in line[::1]]
      #print line
    
    output = str(answer)
    
    print("Case #"+str(t+1)+": "+output)
