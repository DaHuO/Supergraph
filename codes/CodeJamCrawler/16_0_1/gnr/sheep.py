

def find_last_name(n):
    if n == 0:
        return 'INSOMNIA'
    checkset = set()
    curr = n
    count = 1
    while True:
        str_curr = str(curr)
        for ch in str_curr:
            checkset.add(int(ch))
            if len(checkset) == 10:
                return str_curr
        count = count + 1
        curr = n * count


with open('A-large.in') as in_file:
    t = int(in_file.readline())
    with open('out-Alarge.txt', 'w') as out_file:
        for i in xrange(1, t+1):
            n = int(in_file.readline().strip())
            lastname = find_last_name(n)
            out_file.write('Case #{0}: {1}\n'.format(i, lastname))
