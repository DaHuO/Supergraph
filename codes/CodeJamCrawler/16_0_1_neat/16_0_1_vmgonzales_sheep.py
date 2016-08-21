
f = open("A-large.in", "r")
g = open("output.txt", "wb")
line = f.readline()
line = f.readline().rstrip()
case = 1

while line:
    digits = set([0,1,2,3,4,5,6,7,8,9])
    num = int(line)
   
    if(num != 0):
        num = 0
        while (digits):
            num += int(line)
            strNum = str(num)
            while strNum:
                #print case, num, strNum, digits
                digits.discard(int(strNum[0]))
                strNum = strNum[1:]
            
        last = num

    else:
        last = "INSOMNIA"       

    g.write('Case #{}: {}\n'.format(str(case),str(last)))

    line = f.readline().rstrip()
    case += 1

f.close
g.close