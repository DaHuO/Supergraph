def flip_count(s):
    prev = s[0]
    item = s[0]
    n = 0
    for item in s[1:]:
        if item != prev:
            prev = item
            n += 1
    if item == '-':
        n += 1
    return n

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        cakes = str(raw_input())
        print "Case #{}: {}".format(i, flip_count(cakes))

if __name__ == '__main__':
    main()