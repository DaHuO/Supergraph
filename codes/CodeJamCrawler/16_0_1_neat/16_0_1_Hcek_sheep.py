import sys

def name_numbers(N):
    if N == 0:
        return "INSOMNIA"
    else:        
        numbers_seen = set([])
        num = 0

        while(numbers_seen != set([0,1,2,3,4,5,6,7,8,9])):
            num += 1
            numbers_seen |= set([x for x in get_digits(num * N)])

        return str(num * N)

def get_digits(num):
    str_num = str(num)
    for ch in str_num:
        yield int(ch)

data = open(sys.argv[-1]).readlines()

T = data[0]

for index, N in enumerate(data[1:]):
    print 'Case #{0}: {1}'.format(
        index + 1,
        name_numbers(int(N))
    )
