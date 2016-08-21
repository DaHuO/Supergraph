__author__ = 'Alex'

def eliminateplus(sequence):
    count = 0
    #print(sequence[::-1])
    temp = list(sequence[::-1])
    for c in temp: #reverse
        #print('char: ' ,c)
        if c == '+':
            count+=1
        elif c == '-':
            break
    #print('count',count)
    if count == 0:
        return sequence[:]
    return sequence[:-count][:]


def eliminatenegative(sequence):
    count = 0
    #print(sequence[::-1])
    for c in sequence[::-1][:]: #REVERSE
        if c == '-':
            count+=1
        elif c == '+':
            break
    if count == 0:
        return sequence[:]
    return sequence[:-count][:]


#print(eliminateplus('-+-'))
# returns a sequence
def flip(sequence):
    newsequence = ''

    for c in sequence:
        if c == '-':
            newsequence = '+' + newsequence
        elif c == '+':
            newsequence = '-' + newsequence
    #print('flip: ', newsequence)
    return newsequence


#goal is 1 = ++++, 0 = ----
def algorithm(sequence, goal, steps):
    # ignore right most +'s or -'s depending on the goal
    # print('sequence: ',sequence, 'goal: ', goal ,' step: ', steps)
    # print('goal: ',goal)
    # print('step: ',steps)
    if goal == '+':
        # eliminate right most +'s
        newsequence = eliminateplus(sequence)[:]
        if newsequence == '':
            return steps

        # if ends are - XXX -, flip, if goal is +
        if newsequence.startswith('-'):
            return algorithm(flip(newsequence),goal,steps+1)
        # if ends are + XXX -, if goal is +
        elif newsequence.startswith('+'):
            return algorithm(newsequence,'-',steps+1)
        else:
            print('never show')
    else:
        # eliminate right most +'s
        newsequence = eliminatenegative(sequence)[:]
        #print(sequence)
        if newsequence == '':
            return steps

        # if ends are - XXX -, flip, if goal is +
        if newsequence.startswith('+'):
            return algorithm(flip(newsequence),goal,steps+1)
        # if ends are + XXX -, if goal is +
        elif newsequence.startswith('-'):
            return algorithm(newsequence,'+',steps+1)




i = 0
with open("C:/Users/Alex/Downloads/B-large.in","r") as f:
    for line in f:
        if i != 0:
            #print('line:',line)
            print('Case #%s: %s'%(i,algorithm(line[:-1],'+',0)))
        i+=1

