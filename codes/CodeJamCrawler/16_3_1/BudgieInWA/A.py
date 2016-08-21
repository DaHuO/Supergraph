import sys

def print_name(i):
    print(chr(ord('A') + i), end='')

T = int(sys.stdin.readline())

for t in range(T):
    print("Case #{}:".format(t+1), end='')

    N = int(sys.stdin.readline())
    
    counts = [int(v) for v in sys.stdin.readline().split(' ')]

    while True:
        total = 0
        best = 0
        best_i = 0
        people = 0
        for i, c in enumerate(counts):
            people += c
            if c > 0:
                total += 1
            if c > best:
                best = c
                best_i = i

        if best > people - best:
            print("DANGER")

        if total == 0:
            break;

        if total == 2:
            print(' ', end='')
            for i, c in enumerate(counts):
                if c > 0:
                    print_name(i)
                    counts[i] -= 1

        else:
            print(' ', end='')
            print_name(best_i)
            counts[best_i] -= 1

    print()
