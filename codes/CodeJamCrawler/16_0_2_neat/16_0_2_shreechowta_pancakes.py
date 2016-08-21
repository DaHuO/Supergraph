import sys

lines = [x.strip() for x in list(sys.stdin.readlines())]

def count(stack):
    if len(stack) == 1:
        if stack == ['-']:
            return (1)
        else:
            return (0)

    else:
        ordered=False
#         ideal = list('+'*len(stack))
        flips = 0

#         print (''.join(stack))
        while not ordered:
            for i in range(len(stack)-1):
#                 print ('comparing {} and {}'.format(stack[i], stack[i+1]))
                if stack[i] != stack[i+1]:
                    stack[:i+1] = stack[i+1] * (i+1)
#                     print (''.join(stack))
                    flips += 1
                    break
            if i == (len(stack) - 2):
                if stack[i] == '-':
#                     print ('flipping all "-"s... ')
                    flips += 1
#                 print ('went through everything... stack: '.format(stack))

                ordered = True

        return (flips)

cases = int(lines[0])
lines = lines[1:]

for i in range(cases):
    print ('Case #{}: {}'.format(i+1, count(list(lines[i]))))
