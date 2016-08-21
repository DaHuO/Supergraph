import sys


def main():
    f = open(sys.argv[1], "r")
    T = int(f.readline())

    for t in range(1, T + 1):
        S = f.readline().strip()
        last = S[0]
        for i in range(1, len(S)):
            if ord(S[i]) >= ord(last[0]):
                last = S[i] + last
            else:
                last += S[i]

        print('Case #%d: %s' % (t, last))

main()