import sys

test_cases = open(sys.argv[1], 'r')
n = -1
i = 1

for test in test_cases:
    if n == -1:
        n = int(test)
        continue

    text = test.replace('\n', '').replace('\r', '')
    text = text[::-1]
    flips = 0
    index = 0
    current = text[0]
    for char in text:
        if index == 0 and char == '-':
            flips += 1
            index += 1
            continue
        elif index == 0:
            index +=1
            continue
        if not current == char:
            flips += 1
            current = char

    print("Case #" + str(i) + ":", flips)
    i+=1