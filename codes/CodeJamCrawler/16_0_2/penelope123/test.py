f = open('B-large.in')
length = int(f.readline())
stacks = [f.readline().strip() for i in range(length)]

for i, stack in enumerate(stacks):
    # print stack
    flipped = stack[::-1]
    # print flipped
    initial = '+'
    count = 0
    for pancake in flipped:
        if pancake != initial:
            count += 1
            initial = pancake

    print "Case #%s: %s" % (i+1, count)
