import sys
import itertools

sys.stdin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')

obj = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


def main():
    T = int(raw_input())

    for t in range(T):
        out = "Case #%d: " % (t + 1)
        N = int(raw_input())

        if N == 0:
            out += "INSOMNIA"
            print(out)
            continue

        track = {int(i) for i in str(N)}
        to_find = obj.difference(track)
        for i in itertools.count(start=2):
            M = i * N
            for i in str(M):
                track.add(int(i))
            to_find = obj.difference(track)
            if len(to_find) == 0:
                break

        out += str(M)
        print(out)


if __name__ == '__main__':
    main()
