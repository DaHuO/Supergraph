def remain(base_num):
    if base_num == 0:
        return "INSOMNIA"

    remaining = {}
    for i in range(0, 10):
        remaining[i] = None

    i = 1
    while i < 10e6:
        cur_num = str(base_num*i)

        for num_char in cur_num:
            n = int(num_char)
            if n in remaining:
                remaining.pop(n)
                if len(remaining) == 0:
                    return cur_num

        i += 1

    return "INSOMNIA"

def main():
    with open("testlarge.in") as infile:
        N = int(infile.readline())

        for i in range(N):
            num = int(infile.readline().strip())
            print "Case #" + str(i+1) + ": " + remain(num)

if __name__ == "__main__":
    main()
