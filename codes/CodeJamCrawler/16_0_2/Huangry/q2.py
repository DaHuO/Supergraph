with open('B-large (2).in', 'r') as f:
    with open('q2solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            pancake = f.readline()
            stacks = 0
            in_neg = False
            for letter in pancake:
                if letter == '-' and not in_neg:
                    in_neg = True
                    stacks += 1
                if letter == '+':
                    in_neg = False
            flips = 2*stacks

            if pancake[0] == '-':
                flips -= 1
            solution.write('Case #' + str(case+1) + ': ' + str(flips) + '\n')
