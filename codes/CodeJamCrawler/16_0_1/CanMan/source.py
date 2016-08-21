
def printCase(val, i, out):
    out.write('Case #' + str(i) + ': ' + str(val) + '\n')
    return

f = open('C:\Users\Brian\Documents\Pythonscratch\GoogleCodeJam2016\Qualifiers\Problem1\A-large.in', 'r')
first = f.readline()
out = open('C:\Users\Brian\Documents\Pythonscratch\GoogleCodeJam2016\Qualifiers\Problem1\A-large.out', 'w')

i = 1
for line in f:
    original = int(line);
    val = original
    foundList = [0,0,0,0,0,0,0,0,0,0]
    k = 1
    if original == 0:
        val = 'INSOMNIA'
        printCase(val, i, out)
        i += 1
        continue
    else:
        notDone = 1
        while notDone:
            digits = list(str(val))
            #print digits
            for digit in digits: # loop checking digits in current val
                if not notDone:
                    break
                foundList[int(digit)] = 1
                #print foundList
                count = 0
                for j in foundList: # loop checking digits found
                    if j == 1:
                        count += 1
                        if count == 10:
                            printCase(val, i, out)
                            i += 1
                            notDone = 0
                            break
                        continue
                    else: 
                        break # logic here????
            k += 1
            val = k * original
print 'done'
    
