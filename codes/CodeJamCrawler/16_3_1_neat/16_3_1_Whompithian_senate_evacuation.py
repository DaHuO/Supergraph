#!/usr/bin/env python3

import sys

def main():
    output = []
    i = 1
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    for line in lines[2::2]:
        a = evac(line.split())
        output.append('Case #{}: {}\n'.format(i, a))
        i += 1
    with open('output.txt', 'w') as f:
        for o in output:
            f.write(o)

def evac(p):
    A = []
    B = []
    for P in p:
        B.append(int(P))
    while True:
        top = 0
        mid = 0
        low = 0
        for i in range(len(B)):
            if B[i] > B[top]:
                low,  mid, top = mid, top, i
            elif B[i] >= B[mid] or mid == top:
                low, mid = mid, i
            elif B[i] >= B[low] or low == mid:
                low = i
        if B[top] - B[mid] > 1:
            A.append(chr(ord('A') + top) * 2)
            B[top] -= 2
        elif B[top] == B[mid] and top != mid:
            if B[mid] > B[low] or low == mid or low == top:
                A.append(chr(ord('A') + top) + chr(ord('A') + mid))
                B[top] -= 1
                B[mid] -= 1
            elif mid != low:
                if B[mid] > 1:
                    A.append(chr(ord('A') + mid) * 2)
                    B[mid] -= 2
                else:
                    A.append(chr(ord('A') + mid))
                    B[mid] -= 1
        elif B[mid] > B[low] and top != mid:
            A.append(chr(ord('A') + top))
            B[top] -= 1
        else:
            A.append(chr(ord('A') + top))
            B[top] -= 1
        if B[top] == 0:
            break
    return ' '.join(A)

if __name__ == "__main__":
    main()
