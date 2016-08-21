def count_sheep(N):
    if N == 0:
        return 'INSOMNIA'
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lastN = N
    while len(digits) > 0:
        strN = str(lastN)
        for c in strN:
            if len(digits) > 0:
                try:
                    print "Removing " + c
                    digits.remove(c)
                except ValueError:
                    "Do Nothing"
        lastN = lastN + N
    return lastN - N

# Open input file
file_in = open("input.txt", "r")
file_out = open("output.txt", "w")

T = int(file_in.readline())
print "Total test cases: " + str(T)

for i in xrange(T):
    N = int(file_in.readline().rstrip('\n'))
    print "Test case: " + str(i+1) + " - N: " + str(N) + " Length: " + str(len(str(N)))
    out = str(count_sheep(N))
    file_out.write("Case #" + str(i+1) + ": " + out + '\n')
    print out

#Close file
file_in.close()
file_out.close()