def flip(char):
    if char == '-':
        return '+'
    else:
        return '-'

f = open('B-large.in', "r")
o = open('output.txt', "w")
numCases = int(f.readline())
for case in range(1, numCases + 1):
    count = 0
    input = f.readline()
    allPlus = all(value == '+' or value == '\n' for value in input)
    while(not allPlus):
        # Find the last place a minus shows up
        i = input.rfind('-')
        if input[0] == '-':
            temp1 = (input[0:i+1])
            temp = (temp1)[::-1]
            input = temp + input[i+1:]
            input = list(input)
            for k in range (0, i+1):
                input[k] = flip(input[k])
            input = "".join(input)
        else: # First char = '+'
            lastPlus = (input[0:i]).rfind('+')
            temp2 = (input[0:lastPlus+1])
            temp = temp2[::-1]
            input = temp + input[lastPlus+1:]
            #input = (input[0:lastPlus+1])[::-1] + input[lastPlus:]
            input = list(input)
            for k in range (0, lastPlus+1):
                input[k] = flip(input[k])
            input = ''.join(input)
        allPlus = all(value == '+' or value == '\n' for value in input)
        count += 1
    o.write("Case #" + str(case) + ": " + str(count) + "\n")