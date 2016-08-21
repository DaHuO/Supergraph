
# Take input
infile = open('A-large.in', 'r')
lines = infile.readlines()
infile.close()

outfile = open('A-large-out.txt', 'w')

for x, line in enumerate(lines):
    if x == 0:
        numTests = int(line)
    else:
        start = int(line)
        print(start)
        if start == 0:
            # Trivial case
            result = "INSOMNIA"
        else:
            counter = 1
            digitset = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

            while digitset != set():
                currentNum = start * counter
                print(currentNum)
                for digit in str(currentNum):
                    digitset.discard(int(digit))
                    print(digitset)
                counter += 1
                currentNum *= counter

            result = currentNum//counter # revert the last mulitplication

        # Write output
        outfile.write('Case #' + str(x) + ': ' + str(result))
        if x < numTests:
            outfile.write('\n')

outfile.close()
