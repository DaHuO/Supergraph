def main():
    T = input()
    for t in range(T):
        S = raw_input()
        effective = S[:S.rfind('-')+1]
        previous = None
        count = 0
        for c in effective:
            if c == previous: continue
            previous = c
            count += 1
        print "Case #%d: %d" % (t + 1, count)

if __name__ == '__main__': main()