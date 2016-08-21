"""
Counting Sheep

Limits

1 <= T <= 100.  
0 <= N <= 200.  Small dataset
0 <= N <= 10^6. Large dataset

y is the last number that Bleatrix will name before falling asleep
print INSOMNIA if she will count forever

"""

input_file_name = 'A-small-attempt0.in'
output_file_name = 'small_sheep.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w', 0)

# get T, the number of test cases
T = f.readline()
T = int(T)

for t in range(T):
    N = f.readline()    
    N = N.strip()

    if int(N) == 0:
        y = 'INSOMNIA'
    else:
        N_value = int(N)
        digits = [0,0,0,0,0,0,0,0,0,0]
        allFound = False
        multiplier = 1
        while (not allFound):
            # print 'N =', N
            length = len(N)            
            # loop through all of the digits in N
            for i in range(length):
                ch = N[i]
                value = int(ch)
                # loop through the digits array
                for d in range(len(digits)):
                    if value == d:
                        if digits[d] == 0:
                            digits[d] = 1

            # print digits        
            total = sum(digits)
            # print 'total', total
            allFound = (total == 10)
            # print allFound
            if allFound:
                break
            multiplier += 1
            next = N_value * multiplier
            N = str(next)

        if allFound:
            y = N        

    print 'Case #%d:' % (t+1), y
    outFile.write('Case #' + str(t+1) + ': ' + str(y) + "\n")

    



