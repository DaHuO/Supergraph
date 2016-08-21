from collections import defaultdict
from itertools import repeat

unique_chars = [('Z', 0, 'O'),
                ('W', 2, 'O'),
                ('U', 4, 'FO'),
                ('X', 6, 'SI'),
                ('G', 8, 'IH'),
                ('O', 1, ''),
                ('S', 7, ''),
                ('H', 3, ''),
                ('F', 5, 'I'),
                ('I', 9, '')]

for tc in range(1, int(input()) + 1):
    string = input()
    char_counts = defaultdict(int)
    digit_counts = [0 for _ in range(10)]
    for ch in string:
        char_counts[ch] += 1

    for ch, num, removals in unique_chars:
        count = char_counts[ch]
        digit_counts[num] = count
        for rch in removals:
            char_counts[rch] -= count

    print('Case #', tc, ': ', sep='', end='')
    for num, count in enumerate(digit_counts):
        print(*repeat(num, times=count), sep='', end='')
    print()