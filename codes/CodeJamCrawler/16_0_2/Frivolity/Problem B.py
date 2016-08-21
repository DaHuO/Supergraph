#
# The optimal strategy is to flip the top part of the stack that
# is all the same face, thus making that part of the stack larger.
#
# As such, you need as many flips as there are side changes, plus
# one more if the last pancake starts with a blank side up
#

inputFile = open("B-large.in")
outputFile = open("B-large.out", "w")

i = 0

for line in inputFile:
    if i > 0:
        flips = 0
        last = line[0]

        l = line
        if l[-1] == '\n': #remove new line
            l = l[:-1]
            
        for pancake in l:
            if pancake != last:
                flips += 1
                last = pancake

        if last == '-':
            flips += 1

        outputFile.write("Case #" + str(i) + ": " + str(flips) + "\n")
    i += 1
    
inputFile.close()
outputFile.close()
