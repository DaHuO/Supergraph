import sys
import itertools
goal = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' }

file = open(sys.argv[1])
output = open('output.txt', 'w')
nTests = int(file.readline())
testNb = 1
for line in itertools.islice(file, 0, nTests+1):     
    n = int(line)

    if n == 0:
         output.write('Case #' +  str(testNb) + ': ' + 'INSOMNIA' + '\n')
    else:
        found_digits = set(str(n))
        cpt = 2
        last_val = n
        while len(found_digits.symmetric_difference(goal)) != 0 :
            last_val = n * cpt
            found_digits.update(set(str(last_val)))
            cpt += 1
        output.write('Case #' +  str(testNb) + ': ' + str(last_val) + '\n')

    testNb += 1

   