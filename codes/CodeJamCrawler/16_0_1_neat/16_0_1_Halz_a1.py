inp = [0,1,2,11,1692]
out = ['INSOMNIA', 10, 90, 110, 5076]

for i in range(int(raw_input())):
    numb_set = {' '}
    num = int(raw_input())
    for j in range(1000):
        if num == 0:
            case = 'INSOMNIA'
            break
        else:
            number = num * (j + 1)
            numbers = set(str(number) + ' ')
            numb_set.update(numbers)
        if len(numb_set) == 11:
            case = number
            break
    print 'Case #%s: %s' % ((i+1), case)
