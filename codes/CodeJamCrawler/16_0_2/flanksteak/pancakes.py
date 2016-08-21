import sys

def do_test_case(fd):
    tokens = fd.readline().split()

    pancakes = tokens[0]
    chars = []

    for c in pancakes:
        chars.append(c);

    moves = 0

    while True:
        done = False
        if chars[0] == '-':
            for i in xrange(0,len(chars)):
                if chars[i] == '+':
                    break;
                chars[i] = '+';
            moves += 1
        else:
            done = True
            for i in xrange(1,len(chars)):
                if chars[i] == '-':
                    chars[i] = '+'

                    done = False   

                    # last char, flip entire string
                    if i == len(chars)-1:
                        moves += 2
                        done = True
                        break
                    
                    # found the flip point, flip and go
                    if chars[i+1] == '+':
                        moves += 2
                        break

        if done:
            break

    print moves


##################
file = sys.argv[1]

fd = open(file, 'r')

num_tests = fd.readline()

for i in xrange(1,int(num_tests)+1):
    sys.stdout.write("Case #%d: " % (i))
    do_test_case(fd)

