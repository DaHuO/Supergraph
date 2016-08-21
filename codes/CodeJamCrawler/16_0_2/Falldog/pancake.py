import sys

def do_reverse(state, idx, to):
    first = state[idx]
    count = 0
    i = idx - 1
    while i >= 0:
        if state[i] == first:
            i -= 1
        else:
            count = do_reverse(state, i, first)
            break

    if first == to:
        return count
    else:
        return count + 1

def reverse_pan_cake(state):
    state = [c for c in state]
    return do_reverse(state, len(state)-1, '+')

def main():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        count = int(f.readline())
        for i in range(count):
            state_str = f.readline().strip()
            num = reverse_pan_cake(state_str)
            print 'Case #%d: %s' % (i+1, num)
    

if __name__ == '__main__':
    main()
