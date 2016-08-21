
def count(n):
    if n==0:
        return "INSOMNIA"
    temp = 0
    s = set()
    while len(s)!=10:
        temp += n
        s.update(str(temp))
    return temp

with open('A-large.in') as input_file:
    with open('A-large.out', 'w') as output_file:
        T = int(input_file.readline())

        for t in range(1, T+1):
            n = int(input_file.readline())
            if t!=T:
                output_file.write('Case #{}: {}\n'.format(t, count(n)))
            else:
                output_file.write('Case #{}: {}'.format(t, count(n)))