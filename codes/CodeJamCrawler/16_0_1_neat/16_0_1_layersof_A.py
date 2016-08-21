def solve(N):
    if N == 0:
        return "INSOMNIA"
    else:
        flags = [False for i in range(10)]
        i = 1
        while True:
            cur_num = N*i
            cur_str = str(cur_num)
            for c in cur_str:
                flags[ord(c) - ord('0')] = True
            # print cur_str, [j for (j, f) in enumerate(flags) if f]
            if all(flags):
                return cur_num
            i += 1

def main():
    T = input()
    for i in range(T):
        N = input()
        print "Case #%d: %s" % (i+1, solve(N))

#

if __name__ == '__main__':
    main()
