###
 # Google Code Jam
 # Author Rebecca Chen
###
 
input_file = open('C-large.in', 'r')
output_file = open('C-large.out', 'w')
 
num_cases = int(input_file.readline())

for i in range(num_cases):
    output_file.write('Case #' + str(i+1) + ':')

    n, j = [int(x) for x in input_file.readline().split(' ')]
    jamcoins = set()
    def add(coin):
        if coin[-1] == '1':
            jamcoins.add(coin)
    coins = ['1001']
    while len(jamcoins) < j and len(coins) > 0:
        coin = coins.pop()
        diff = n - len(coin)
        if diff == 0:
            add(coin)
        elif diff == 1:
            continue
        elif diff == 2:
            add('11' + coin)
            add(coin + '11')
        elif diff == 3:
            add('110' + coin)
            add(coin + '110')
        elif diff == 4:
            add('1111' + coin)
            add('11' + coin + '11')
            add(coin + '1111')
            add('1001' + coin)
            add(coin + '1001')
        else:
            coins.append('11' + coin)
            coins.append(coin + '11')
            coins.append('110' + coin)
            coins.append(coin + '110')
            coins.append('1001' + coin)
            coins.append(coin + '1001')
    for jamcoin in list(jamcoins)[:j]:
        output_file.write('\n' + str(jamcoin) + ' 3 2 5 3 7 2 3 5 11')

    output_file.write('\n')
     
input_file.close()
output_file.close()
