tc = input()
for tcn in range(tc):
    cakes = raw_input()
    plus = '+'
    minus = '-'
    steps = 0
    cakes = list(cakes)
    last_item = cakes[0]
    total_chars = len(cakes)
    if len(cakes) == 1:
        if cakes[0] == plus:
            print 'Case #' + str(tcn+1) + ': ' + '0'
        elif cakes[0] == minus:
            print 'Case #' + str(tcn+1) + ': ' + '1'
    else:
        for i in range(0, total_chars):
            item = cakes[i]
            if i == 0:
                last_item = item
            else:
                last_item = cakes[i-1]
            if i != 0 and item == plus and last_item == plus:
                continue
            elif i != 0 and item == minus and last_item == minus:
                # handle end case
                continue
            elif item != last_item:
                # flip the prev
                steps = steps + 1
                for j in range(len(cakes[:i])):
                    if cakes[j] == minus:
                        cakes[j] = plus
                    else:
                        cakes[j] = minus
                i = 0
            if ''.join(cakes) == '-' * total_chars:
                steps = steps + 1

        print 'Case #' + str(tcn+1) + ': ' + str(steps)
