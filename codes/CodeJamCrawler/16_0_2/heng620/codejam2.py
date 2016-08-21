import re, sys
array = []
with open('input.txt') as f:
    numCases = int(next(f).split()[0]) # read first line
    for line in f: # read rest of lines
        array.append([str(x) for x in line.split()][0])

counts = [0]*numCases

print("numCases: " + str(numCases))
print(array)
swap = {'+' : '-', '-' : '+'}

def flipTopPancakes(bottom, string):
    substr = string[0:bottom:]
    substr = substr.replace("+", "0")
    substr = substr.replace("-", "+")
    substr = substr.replace("0", "-")
    return substr[::-1]+string[bottom::]


for index, value in enumerate(array):
    stack = value
    if "-" not in value:
        counts[index] = 0
        continue
    
    while (stack != '+'*len(stack)):
        if stack[0] == '+':
            try:
                stack = flipTopPancakes(stack.index('-'), stack)
                counts[index] += 1
            except:
                break
        elif stack[0] == '-':
            try:
                stack = flipTopPancakes(stack.index('+'), stack)
                counts[index] += 1
            except:
                stack = flipTopPancakes(len(stack), stack)
                counts[index] += 1
        #print("index: " + str(index) + " counts: " + str(counts[index]))
        #print(stack)



with open('output.txt', 'w') as out:
    for index, value in enumerate(array):
        print(str("Case #" + str(index+1) + ": " + str(counts[index])))
        out.write(str("Case #" + str(index+1) + ": " + str(counts[index])) + '\n')

