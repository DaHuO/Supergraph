file1 = "A-large.in.txt"
file = open(file1, "r")
attempt = int(file.readline().strip())
numAttempt = 1
while(numAttempt != attempt + 1):
     #global numAttempt
     print("Case #", end='')
     print(numAttempt, end="")
     print(": ",end="")
     case = int(file.readline().strip())
     if case == 0:
          print("INSOMNIA")
          numAttempt += 1
     else:
          digits = set()
          this_case = case
          while(len(digits) != 10):
               digits = digits.union(set(str(this_case)))
               this_case += case
               #print(this_case)
               #print(digits)
          case = this_case  - case
          print(case)
          numAttempt += 1
          
