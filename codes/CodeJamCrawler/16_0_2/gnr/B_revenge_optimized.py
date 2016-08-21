__author__ = 'dilip'

def flip(end_index, root, l):
    if root == '+':
        replacechar = '-'
    else:
        replacechar = '+'
    for i in xrange(end_index):
        l[i] = replacechar

def findsteps(s):
    chlist = [ch for ch in s]
    root = ''
    count = 0;
    isDone = False

    while not isDone:
        root = chlist[0]  # mark first char as root
        for i, ch in enumerate(chlist):
            # loop until you reach where root does not match
            if ch == root:
                if len(chlist) - 1 == i:# all the chars till end are same
                    if root == '-':
                        flip(i, root, chlist)
                        count = count + 1
                    isDone = True
                    break
            else:
                flip(i, root, chlist)
                count = count + 1
                break
    return count

def find_steps_optimized(s):
    chlist = [ch for ch in s]
    root = ''
    count = 0;
    isDone = False

    root = chlist[0]
    if root == '+':
        happyside = True
    else:
        happyside = False
    for ch in chlist:
        if ch != root:
            count = count + 1
            happyside = not happyside
            root = ch
    if not happyside:
        count = count + 1


with open('B-large.in') as in_file:
    t = int(in_file.readline())
    with open('B-large.out', 'w') as out_file:
        for i in xrange(1, t+1):
            s = in_file.readline().strip()
            count = findsteps(s)
            out_file.write('Case #{0}: {1}\n'.format(i, count))