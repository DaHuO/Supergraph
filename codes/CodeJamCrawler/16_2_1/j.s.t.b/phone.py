import collections

filename = "A-large"
#filename = "A-minimal"

with open(filename + ".in", 'r') as inputfile:
    lines = inputfile.readlines()

with open(filename + ".out", 'w') as outputfile:
    number_of_tests = 0
    for linenumber, line in enumerate(lines):
        if linenumber == 0:
            number_of_tests = int(line.strip())
            print("There are {} tests".format(number_of_tests))
        elif linenumber > number_of_tests:
            break
        else:
            casenumber = linenumber
            n = [0]*10
            print("\n\n*** Testcase {} ***".format(casenumber))
            inputcharacters = sorted(line.strip())
            print("Characters: {}".format(inputcharacters))
            cc = collections.Counter(inputcharacters)
            assert sum(cc.values()) == len(inputcharacters)
            #print(cc)
            
            n[0] = cc['Z']
            cc.subtract("ZERO"*n[0])
            #print("ZERO removed", cc)
                
            n[2] = cc['W']
            cc.subtract("TWO"*n[2])
            #print("TWO removed", cc)
            
            n[4] = cc['U']
            cc.subtract("FOUR"*n[4])
            #print("FOUR removed", cc)
            
            n[6] = cc['X']
            cc.subtract("SIX"*n[6])
            #print("SIX removed", cc)
            
            n[8] = cc['G']
            cc.subtract("EIGHT"*n[8])
            #print("EIGHT removed", cc)

            n[5] = cc['F']
            cc.subtract("FIVE"*n[5])
            #print("FIVE removed", cc)

            n[3] = cc['H']
            cc.subtract("THREE"*n[3])
            #print("THREE removed", cc)

            n[7] = cc['V']
            cc.subtract("SEVEN"*n[7])
            #print("SEVEN removed", cc)

            n[1] = cc['O']
            cc.subtract("ONE"*n[1])
            #print("ONE removed", cc)

            n[9] = cc['I']
            cc.subtract("NINE"*n[9])
            #print("NINE removed", cc)

            assert sum(cc.values()) == 0

            phonenumber = ""
            for i, v in enumerate(n):
                for j in range(v):
                    phonenumber += str(i)

            answer = "Case #{}: {}\n".format(casenumber, phonenumber)
            print(answer)
            outputfile.write(answer)
