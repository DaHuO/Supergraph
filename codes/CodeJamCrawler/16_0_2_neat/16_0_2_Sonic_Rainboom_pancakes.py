import sys

def flip(string, pos):
    if string[0] == '-':
        new = ""
        for num in range(pos, -1, -1):
            if string[num] == '+':
                new += '-'
            else:
                new += '+'
        ans = new[0:pos + 1] + string[pos + 1:]
        return (ans, 1)
    else:
        index = 0
        while string[index] == '+':
            index += 1
        new = ""
        for num in range(0, index):
            new += '-'
        string = new[0:index] + string[index:]
        #print string
        new = ""
        for num in range(pos, -1, -1):
            if string[num] == '+':
                new += '-'
            else:
                new += '+'
        ans = new[0:pos + 1] + string[pos + 1:]
        return (ans, 2)
            

def pancakes(string):
    #print "##################"
    flips = 0
    for pos in range(len(string) - 1, -1, -1):
        if string[pos] == '+':
            continue
        else:
            #print string
            tup = flip(string, pos)
            string = tup[0]
            flips += tup[1]
    #print string
    return flips

    
in_file = open("B-large.in", 'r')
out_file = open("output.txt", 'w')

size = int(in_file.readline())

case = 1

while case <= size:
    line = in_file.readline().strip()
    #sys.stdout.write(line.strip())
    flips = pancakes(line)
    #sys.stdout.write("\t\t")
    answer = "Case #" + str(case) + ": " + str(flips) + "\n" 
    out_file.write(answer)
    case += 1

in_file.close()
out_file.close()

