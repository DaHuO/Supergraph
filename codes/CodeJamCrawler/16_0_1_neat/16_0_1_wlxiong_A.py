import sys
import multiprocessing


def count(N):
    if N == 0:
        return None
    w = len(str(N))
    digits = set(map(str, range(0, 10)))
    MAX = 1000000
    for i in range(1, MAX+1):
        for c in str(i * N):
            digits.discard(c)
            if not digits:
                return i * N
    return None


def main():
    T = int(sys.stdin.readline())
    inputs = [int(sys.stdin.readline()) for _ in range(1, T+1)]
    p = multiprocessing.Pool(multiprocessing.cpu_count() / 2)
    outputs = p.map(count, inputs)
    for t, c in enumerate(outputs):
        print "Case #%d:" % (t + 1),
        print "INSOMNIA" if c is None else c


if __name__ == '__main__':
    main()
