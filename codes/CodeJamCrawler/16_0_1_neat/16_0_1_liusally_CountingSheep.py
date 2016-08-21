
complete_value = 1023
of = open('count-large.out','w')

with open('A-large.in', 'r') as f:
    count = int(f.readline().rstrip('\n'))
    for i in range(count):
        str = f.readline().rstrip('\n')
        value = int(str)
        binary_dic = 0

        if value != 0:
            j = 1
            last_num = 0
            while not (binary_dic == complete_value):
                n = value * j
                last_num = n
                while n:
                    digit = n % 10
                    n //= 10
                    binary_num = 1 << digit
                    binary_dic |= binary_num
                j = j + 1

            of.write('Case #{}: {}\n'.format(i + 1, last_num))
        else:
            of.write('Case #{}: INSOMNIA\n'.format(i + 1))

of.close()



