"""Counting Sheep"""
with open("A-small-attempt0.in") as f:
    out = open("out-counting-sheep.in","w")
    T = int(f.readline())
    
    for i in range(1, T + 1):
        numbers = {'0': False, '1': False, '2':False, '3':False, '4': False, '5':False, '6': False, '7': False, '8': False, '9': False}
        N = f.readline().strip()
        found = False
        factor = 1
        P = N
        while not found:
            if P == '0':
                break                
            elif len(P) == 1:
                numbers[P] = True
            elif len(P) > 1:
                digits = list(P)
                for dig in digits:
                    numbers[dig] = True

            for v in numbers.values():
                if v == False:
                    factor += 1
                    P = str(int(N) * factor)
                    break
            else:
                found = True

        out.write("Case #{}: {}".format(i, 'INSOMNIA' if P == '0' else P) + ("\n","")[i == T])
        #print("Case #{}: {}".format(i, 'INSOMNIA' if P == '0' else P))
    out.close()
print("done")