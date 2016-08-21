def flip_pancakes(t, line):
    flips = 0
    lastcake = ''
    for pancake in line:
        if(lastcake != '' and pancake != lastcake):
            flips += 1
        lastcake = pancake

    if(lastcake == '-'):
        flips += 1

    print('Case #{}: {}'.format(t, flips))

def main():
    with open('B-large.in', 'r') as f:
        for line_num, line in enumerate(f):
            if(line_num != 0):
                flip_pancakes(line_num, line.rstrip())
        pass

if __name__ == '__main__':
    main()
