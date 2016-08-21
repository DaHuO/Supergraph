cases = int(input())
for i in range(cases):
    case = int(input())
    if case == 0:
        result = None
    else:
        running = True
        current = 0
        digits = [0,0,0,0,0,0,0,0,0,0]
        while(running == True):
            current += case
            currentArray = str(current)
            for digit in currentArray:
                digits[int(digit)] += 1
            if(min(digits)>0):
                running = False
                result = current
    if(result):
        print("Case #"+str(i+1)+": "+str(result))
    else:
        print("Case #"+str(i+1)+": INSOMNIA")