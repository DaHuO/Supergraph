fin = open('B-large.in', 'r')

N = int(fin.readline())
stacks = map(lambda x: list(x.rstrip()), fin.readlines())

# print N
# print stacks

def flip(s):
    r = s[::-1]
    for i,char in enumerate(r):
        if char == '+':
            r[i] = '-'
        else:
            r[i] = '+'
    return r

def remove_end(s):
    if len(s) > 0:
        while s[-1] == '+':
            s.pop()
            if len(s) == 0:
                break
    return s

result = []
for s in stacks:
    this_stack = remove_end(s)
    count = 0
    while '-' in this_stack:
        if this_stack[0] == '-':
            this_stack = flip(this_stack)
            this_stack = remove_end(this_stack)
            count += 1
        else:
            for i in range(len(this_stack)):
                if this_stack[i] == '+':
                    this_stack[i] = '-'
                else:
                    break
            this_stack = remove_end(this_stack)
            count += 1
    result.append(count)

#print flip(['-','-','+','-'])
#print result
fin.close()

fout = open('B-large.out', 'w')
for i,r in enumerate(result):
    print >> fout, "Case #" + str(i+1) + ": " + str(result[i])
fout.close()