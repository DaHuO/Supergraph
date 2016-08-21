
import sys
from collections import Counter

def rank_and_file(n, lists):
    all_items = [x for y in lists for x in y]
    counts = Counter(all_items)
    odds = [x for x in counts if counts[x] % 2 != 0]
    return sorted(odds)

def main():
    t = int(sys.stdin.readline().strip())
    for k in range(t):
        n = int(sys.stdin.readline().strip())
        lists = []
        for j in range(2*n-1):
            line = sys.stdin.readline().strip()
            lists.append(map(int, line.split()))
        solution = rank_and_file(n, lists)
        print 'Case #' + str(k+1) + ': ' + ' '.join(map(str, solution))

if __name__ == '__main__':
    main()

