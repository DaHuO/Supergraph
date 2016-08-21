import sys
cases = int(raw_input())

for x in range(1, cases+1):
    cakes = list(raw_input())
    count = 0


    stack_size = len(cakes)
    while True:
        ndx = 0
        count += 1
        if cakes[0] == '-':
            for ndx in range(0, stack_size):
                if cakes[ndx] == '-':
                    cakes[ndx] = '+'
                else:
                    break
        elif cakes[0] == '+':
            for ndx in range(0, stack_size):
                if cakes[ndx] == '+':
                    cakes[ndx] = '-'
                else:
                    ndx = -1
                    break
            if ndx == stack_size-1:
                break

    print 'Case #' + str(x) + ': ' + str(count -1)
