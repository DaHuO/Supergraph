#!/usr/bin/python


def solve(sequence):
    flips = 0
    while True:
        if all(i for i in sequence):
            return flips
        elif all(not i for i in sequence):
            return flips + 1
        if sequence[0]:
            flips += 2
        else:
            flips += 1
        for i in range(sequence.index(False), len(sequence)):
            if not sequence[i]:
                sequence[i] = True
            else:
                break
    

def main():
    t = int(input())
    for i in range(1, t + 1):
        sequence = input().strip()
        sequence = [True if c == '+' else False for c in sequence]
        print('Case #{}: {}'.format(i, solve(sequence)))


if __name__ == '__main__':
    main()
