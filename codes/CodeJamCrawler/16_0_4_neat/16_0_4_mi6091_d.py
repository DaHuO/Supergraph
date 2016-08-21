import sys;

def solve(k, c, s):

    if(k == 1):
        return 1;
        return;
    if(c == 1):
        return "IMPOSSIBLE" if s < k else " ".join(map(str, range(1, k+1)));

    temp = 1

    ret = []
    while (temp <= k):
        if(temp != k):
            ret.append((temp - 1)*k + temp + 1);
        else:
            ret.append(temp);
        temp = temp + 2;

    if(len(ret) > s):
        return "IMPOSSIBLE";

    return " ".join(map(str, ret));

if __name__ == "__main__":
    data = sys.stdin.readlines();

    n = int(data[0]);

    for i in range(1, n+1):
        k, c, s = map(int, data[i].split())
        print "Case #{}:".format(i), solve(k, c, s);
