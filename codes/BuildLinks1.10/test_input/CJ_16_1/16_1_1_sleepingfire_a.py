import sys, os
from collections import deque

def main(s):
    q = deque()
    q.append(s[0])
    for i in range(1, len(s)):
        c = s[i]
        if c >= q[0]:
            q.appendleft(c)
        else:
            q.append(c)
    return "".join(q)


if __name__ == "__main__":
    in_path = "test.in" if len(sys.argv) == 1 else sys.argv[1]
    in_file = open(in_path, 'r')
    T = int(in_file.readline().rstrip())

    for case_idx in range(T):
        s = in_file.readline().rstrip()
        res = main(s)
        print("Case #{}: {}".format(case_idx + 1, res))
