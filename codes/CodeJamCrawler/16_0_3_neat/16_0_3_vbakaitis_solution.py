import string, sys, math
sys.stdin.readline()
case = sys.stdin.readline().split()
n = int(case[0])
j = int(case[1])
nm = int(math.pow(2,n-2))
jc = 0
print "Case #1:"
for c in range(nm):
    result = []
    nt = "1" + format(c, '0' + str(n-2) + 'b') + "1"
    for b in range(2, 11): 
       number = int(nt,b)
       for l in range (2,min(number, 200000)):
           if(number % l == 0):
               result.append(str(l))
               break
       if(len(result) < b - 1):
           break;
       elif(len(result) == 9):
            print nt + " " + string.join(result, " ")
            jc += 1
    if(jc == j):
        break
