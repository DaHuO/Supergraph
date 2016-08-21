import copy
import string

PARTIES = string.ascii_uppercase

def evacuation(input_list):
    total = 0
    output = ''
    for integer in input_list:
        total += integer
    next_step = copy.copy(input_list)
    while total > 0:
        first = next_step.index(sorted(next_step, reverse=True)[0])
        second = next_step.index(sorted(next_step, reverse=True)[1])
        next_step[first] -= 2
        if first == second:
            second = next_step.index(sorted(next_step, reverse=True)[0])
        if evaluate(next_step, total-2):
            output += PARTIES[first]*2 + ' '
            total -= 2
        else:
            next_step[first] += 1
            next_step[second] -= 1
            if evaluate(next_step, total-2):
                output += PARTIES[first]+PARTIES[second]
                total -= 2
                if total > 0:
                    output +=  ' '
            else:
                next_step[second] += 1
                if evaluate(next_step, total-1):
                    output += PARTIES[first]
                    total -= 1
                    if total > 0:
                        output +=  ' '
                else:
                    print "HELP"
                    break
                
    return output

def evaluate(input_list, total):
    for thing in input_list:
        if thing < 0:
            return False
    if total == 0:
        return True
    for thing in input_list:
        if thing/float(total) > 0.5:
            return False
    return True

with open("A-large.in", 'r') as ipf, open("senate.txt", 'w') as opf:
    lines = ipf.read().splitlines()
    for i in range(int(lines[0])):
        opf.write("Case #" + str(i+1) + ": ")
        parties = lines[2*(i+1)].split()
        parties = map(int, parties)
        opf.write(evacuation(parties) +"\n")
