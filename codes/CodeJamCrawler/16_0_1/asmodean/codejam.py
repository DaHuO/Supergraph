#t = int(raw_input());
whole = [int(x) for x in raw_input().split('\n')];
t= whole[0];
for i in xrange(1, t + 1):
    digitList =[];
    n = whole[i];
    temp = 0;
    while len(digitList)<10:
        temp +=n;
        if temp == 0:
            temp = "INSOMNIA";
            break;
        for digit in str(temp):
            if digit not in digitList:
                digitList.append(digit);
    print "Case #{}: {}".format(i, temp);