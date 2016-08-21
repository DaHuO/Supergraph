import itertools
file1 = "D-small-attempt1.in.txt"
file = open(file1, "r")
attempt = int(file.readline().strip())
numAttempt = 1
while(numAttempt != attempt + 1):
     print("Case #", end='')
     print(numAttempt, end="")
     print(": ",end="")
     data = file.readline().strip().rsplit(sep=' ')
     number = int(data[0])
     complexity = int(data[1])
     student = int(data[2])
     for i in range(1, number + 1):
          print(i, end=' ')
     print()
     numAttempt += 1
     
     
               
               
     
     
     
     
          
          
