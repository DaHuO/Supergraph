input = open("input.txt", 'r')

tmp = input.readline()
if tmp.strip():
    T = int(tmp)

case = 0
for i in range(0,int(T)):
    case = case + 1
    tmp = input.readline()
    if tmp.strip():
        N = int(tmp)
    parse = str(N)
    digits = [False]*10
    
    added = N
    done = False
    while (done != True):
        if (N == 0):
            break
        done = True
        for char in parse:
            digits[int(char)] = True
        for j in range(0,10):
          if digits[j] == False:
             done = False
        added = added + N
        parse = str(added)
    
    if (N == 0):
        print "Case #" + str(case) + ": INSOMNIA" 
    else:
        print "Case #" + str(case) + ": " + str(added - N)
