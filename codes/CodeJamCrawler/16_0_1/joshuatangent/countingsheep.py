import sys


index = 1

num = input()
for line in sys.stdin.readlines():
    seen = [False, False, False, False, False, False, False, False, False, False]
    num = int(line)

    print("Case #" + str(index), end=': ')
    index += 1

    if num == 0:
        print("INSOMNIA")
        continue

    curnum = num

    for digit in str(curnum):
        seen[int(digit)] = True

    while not (seen[0] and seen[1] and seen[2] and seen[3] and seen[4] and seen[5] and seen[6] and seen[7] and seen[8] and seen[9]):
        curnum += num
        for digit in str(curnum):
            seen[int(digit)] = True

    print(curnum)
