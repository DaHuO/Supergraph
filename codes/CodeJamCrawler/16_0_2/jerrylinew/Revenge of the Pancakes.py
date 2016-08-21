filename = 'B-large-attempt0.out'
target = open(filename, 'w')

t = int(input())

for i in range(t):
    pancakes = input()
    counter = 0
    if pancakes[-1] == '-':
        counter += 1

    index = 1
    while index < len(pancakes):
        if pancakes[index] != pancakes[index - 1]:
            counter += 1
        index += 1

    target.write('Case #%d: %d\n' % (i + 1, counter))

