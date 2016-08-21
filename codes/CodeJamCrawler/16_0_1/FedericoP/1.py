n = int(raw_input())
count = 1

while count <= n:
    case = int(raw_input())
    number = case
    numbers = set([c for c in str(number)])

    if case == 0:
        print 'CASE #{}: '.format(count) + 'INSOMNIA'
        count += 1
        continue
    i = 2
    while len(numbers) < 10:
        number = case * i
        for c in str(number):
            numbers.add(c)
        i += 1

    print 'CASE #{}: '.format(count) + str(number)
    count += 1
