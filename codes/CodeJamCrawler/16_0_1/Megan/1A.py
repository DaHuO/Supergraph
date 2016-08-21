import fileinput

i = 0
num_cases = -1
for line in fileinput.input():
    if (i == 0):
        num_cases = int(line)
    else:
        n = int(line)
        if (n == 0):
            print "Case #" + str(i) +": INSOMNIA"  
        else:
            nums_found = {}
            j = 1
            while (True):
                result = j * n
                temp = result
                while (temp > 0):
                    current = temp%10
                    if not(current in nums_found):
                        nums_found[current] = True
                    temp/=10
                j += 1
                if (len(nums_found.keys()) >= 10):
                    print "Case #" + str(i) + ": " + str(result)
                    break
    i+=1
    if (i > num_cases):
        break