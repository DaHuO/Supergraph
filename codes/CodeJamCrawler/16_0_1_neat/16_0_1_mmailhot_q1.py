
def largest_seen(n):
    original_n = n

    digits_seen = [False] * 10

    if n == 0:
        return 'INSOMNIA'

    while True:
        for digit in map(int, str(n)):
            digits_seen[digit] = True

        if all(digits_seen):
            return n

        n += original_n

with open('/home/mmailhot/Downloads/A-large.in') as f:
    num_lines = int(f.readline())
    for i in range(num_lines):
        print('Case #{}: {}'.format(i + 1, largest_seen(int(f.readline()))))
