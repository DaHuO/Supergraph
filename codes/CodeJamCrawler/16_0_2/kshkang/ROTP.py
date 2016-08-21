#get string
#find the last - sign
#flip there
#keep move left and keep flipping at the - sign

file = open("B-large.in")
numOfCases = int(file.readline().strip("\n"))

answer = open("answer.txt", "w")

# Get Pattern
def getPattern(file):
    return file.readline().strip("\n")


#Find Minus
def findMinus(pattern):
    count = 0
    while "-" in pattern:
        pattern = flip(pattern,pattern.rindex('-'))
        count += 1
    return pattern,count


#Flip Function
def flip(pattern, index):
    pattern = list(pattern)
    for x in range(index + 1):
        if pattern[x] == '+':
            pattern[x] = '-'
        elif pattern[x] == '-':
            pattern[x] = '+'
        else:
            print("Flipping Error")
    return ''.join(pattern)


#Run Program
for case in range(numOfCases):
    pattern = getPattern(file)
    pattern,count = findMinus(pattern)
    answer.write("Case #%s: %s%s" % (case + 1, count, "\n"))

file.close()
answer.close()