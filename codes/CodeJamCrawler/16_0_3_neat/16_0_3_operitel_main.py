from math import floor
file = open('C-large.in', 'r')
output = open('C-large.ou', 'w')

def finddivisor( number ):
    maximum = 2**10 + 1 if floor(number**0.5) > 2**10 + 1 else floor(number**0.5)
    for div in range(3, maximum +1, 2):
        if number % div == 0:
            return div
    return 0

T = file.readline()
i = 1
for line in file:
    line = line.rstrip()

    print('Case #' + str(i) + ':')
    output.write('Case #' + str(i) + ':\n')

    N = int(line.split(' ')[0])
    J = int(line.split(' ')[1])

    count = 0
    jamcoin = 0
    while count < J:
        jamcoin_str = "{0:b}".format(jamcoin)
        jamcoin_str = jamcoin_str.zfill(N - 2)
        jamcoin_str = '1' + jamcoin_str + '1'

        res = jamcoin_str

        prime = False
        for base in range(2, 10+1):
            num = int(jamcoin_str, base)
            div = finddivisor(num)
            if div == 0:
                prime = True
                break
            else:
                res += ' ' + str(div)
        if not prime:
            print(res)
            output.write(res + '\n')
            count += 1

        jamcoin += 1
    i += 1

output.close()
