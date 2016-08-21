import time
infile = open("input2", "r")

outfile = open("output2", "w")

lines = infile.readlines()
linenum = lines[0]

def swap(line, position):
    for j,pancake in enumerate(line[:(position+1)]):
        if pancake == '-':
            line[j] = '+'
        else:
            line[j] = '-'
            
    rev_list = line[:(position+1)]
    rev_list = rev_list[::-1]
    line = rev_list + line[(position+1):]
    return line

for idx,line1 in enumerate(lines[1:]):

    flips = 0
    line = list(line1.rstrip())

    while '-' in line: 
        position = 0
    
        if '+' not in line:
            flips += 1
            break

        for i,pancake in enumerate(reversed(line)):
            if pancake == '-':
                position = len(line)-1-i
                break
        
        if line[0] == '+':
            for j, pancake in enumerate(line):
                if pancake == '-':
                    position2 = j-1
                    break
            line = swap(line, position2)
            flips += 1
            

        line = swap(line, position)
        flips +=1
    outfile.write("Case #" + str(idx+1) + ": " + str(flips) + "\n")
