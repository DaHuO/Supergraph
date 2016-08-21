__author__ = 'Devatanu'
import sys


def flip_stack(stack,num):
    s_start = stack[:num]
    s_end = stack[num:]

    # print s_start,':',s_end
    a = list(s_start)
    a.reverse()
    return (("".join(a)).replace('-','_').replace('+','-').replace('_','+')) + s_end



def make_happy(stack):
    flips = 0
    if '-' not in stack:
        return 0
    elif '+' not in stack:
        return 1
    else:
        while '-' in stack:
            if '+' not in stack:
                flips += 1
                break
            elif stack.startswith('-'):
                stack = flip_stack(stack,stack.find('+'))
                flips += 1
                # print flips, stack
            elif stack.startswith('+'):
                stack = flip_stack(stack,stack.find('-'))
                flips += 1
                # print flips, stack
            else:
                raise TypeError
            # raw_input()
        return flips





if __name__ == '__main__':
    f = sys.stdin
    # print type(f)
    lines = f.readlines()
    cases = int(lines[0])
    for i in range(1,cases+1):
        line = lines[i].strip()
        print "Case #"+str(i)+": " + str(make_happy(line))
    f.close()

    # stack = '++'
    # print stack
    # print make_happy(stack)
