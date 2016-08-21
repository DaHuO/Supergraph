with open('A-large.in') as f:
	with open('A.out', 'w') as out:
            tests = f.readline()
            testNum = 1
            for line in f:
                n = int(line)
                if n == 0:
                    out.write("Case #" + str(testNum) + ": INSOMNIA\n")
                else :
                    a = [0,1,2,3,4,5,6,7,8,9]
                    b = a[:]
                    done = False
                    mult = 1
                    last = 1
                    while not done:
                        last = n * mult
                        
                        for num in a:
                            if num in map(int, str(last)):
                                b.remove(num)
                            if len(b) == 0:
                                done = True
                        a =  b[:]
                        mult += 1
                            
                    out.write("Case #" + str(testNum) + ": " + str(last) + "\n")
                testNum += 1