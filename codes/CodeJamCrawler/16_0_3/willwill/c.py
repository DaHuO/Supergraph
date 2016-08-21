import sys
import itertools
import mathapi

def process(n, j):
    print("Case #1:")

    found = 0
    for item in itertools.product('01', repeat=n-2):
        item = '1{}1'.format(''.join(item))

        valid = True
        for base in range(2, 11):
            item_base = int(item, base)
            if item_base in mathapi.prime:
                valid = False
                break

        if not valid:
            continue

        print(item, end=" ")
        for base in range(2, 11):
            item_base = int(item, base)
            print(mathapi.factorized(item_base)[0], end=" ")
        print()


        found = found + 1
        if found == j:
            break

if __name__ == '__main__':
    sys.stdin.readline()
    n, j = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    process(n, j)
