def check(digits):
    if (0 in digits and 1 in digits and 2 in digits and 3 in digits and 4 in digits and 5 in digits and 6 in digits and 7 in digits and 8 in digits and 9 in digits):
        return 1
    else:
        return 0

if __name__ == '__main__':
    f = open('A-large.in','r')
    o = open('Output.dat','w')
    T = int(f.readline())
    for zz in range(0,T):
        case = "Case #" + str(zz+1) + ": "
        N = int(f.readline())
        i = 1
        digits = list()
        if N == 0:
            case += "INSOMNIA"
        else:
            while(check(digits) != 1):
                number = N*i
                test = str(number)
                for j in range(0,len(test)):
                    if test[j] not in digits:
                        digits.append(int(test[j]))
                i += 1
            case += str(number)
        case += "\n"
        o.write(case)
