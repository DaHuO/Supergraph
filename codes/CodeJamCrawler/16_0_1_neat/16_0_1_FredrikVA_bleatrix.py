__author__ = 'fredrikanthonisen'

from sys import stdin, stderr, stdout

#converter = lambda num: map(int, str(num))

def count_numbers(n):
    seen = []
    base = n
    j = 1
    while len(seen)<10:
        n = j*int(base)
        NUMBERS = [int(x) for x in str(n)]
        for i in NUMBERS:
            if i not in seen:
                seen.append(i)
        j += 1
    return n



numberOfTestcases = int(stdin.readline())
stdout = open('output.txt', 'w')
test_case = 1
for line in stdin:
    line = line.strip()
    if int(line) == 0:
        stdout.write("Case #" + str(test_case) + ": INSOMNIA" + "\n")
    else:
        end_number = count_numbers(line)
        stdout.write("Case #" + str(test_case) + ": " + str(end_number) + "\n")
    test_case += 1