from math import sqrt
f = open('C-Large.in', 'r')
g = open('output_C_Large.txt', 'w')
num_loops = int(f.readline())

for i in range(0,num_loops):
    string = str('Case #' + str(i+1) + ':' + '\n')
    g.write(string)
    currentCase = f.readline().split()
    print(currentCase)
    N = int(currentCase[0])
    J = int(currentCase[1])
    foundJ = []
    while len(foundJ) < J:
        for p in range((2**(N-1))+1,(2**N),2):
            print ("Current: " + str(bin(p)[2:]))
            currentDivisors = []
            for m in range(2,11):
                testInt = int(bin(p)[2:],m)
#                print testInt
                breakPlease = False
                with open("primes.txt") as openfile:
                    for line in openfile:
                        if breakPlease == False:
                            for part in line.split():
                                if int(part) >= (sqrt(int(testInt))+1):
                                    breakPlease = True
                                    break
                                elif int(part) <= (sqrt(int(testInt))+1):
                                    if testInt%int(part) ==0:
                                        currentDivisors.append(str(part))
                                        breakPlease = True
                                        break
                        else:
                            break
            if len(currentDivisors) == 9:
                foundJ.append((str(bin(p)[2:])," ".join(currentDivisors)))
            if len(foundJ) == J: break
    for foo in foundJ:
        print (foo[0] + " " + foo[1])
        string = str(foo[0] + " " + foo[1] + '\n')
        g.write(string)
f.close()
g.close()
