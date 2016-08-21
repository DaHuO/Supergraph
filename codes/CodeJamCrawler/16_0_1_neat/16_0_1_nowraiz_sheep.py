def ones(l):
    for i in l:
        if i == 0:
            return False;
    return True;


def number(num):
    if num == 0:
        return "INSOMNIA";
    seen = [0]*10;

    k = 1;
    while not ones(seen):
        n = k*num;
        for i in str(n):
            seen[int(i)] = 1;
        k = k+1;
    return str(n);


if __name__ == '__main__':
    times = int(raw_input());
    for i in range(1,times+1):
        out = number(int(raw_input()))
        print "Case #"+str(i)+": "+ out
