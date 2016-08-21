def answer(x):
    if x == 0:
        return 'INSOMNIA'
    else:
        seen_numbers = [0] * 10
        num_numbers = 0
        result = 1
        while num_numbers != 10:
            for number in str(x * result):
                if seen_numbers[int(number)] == 0:
                    num_numbers += 1
                    seen_numbers[int(number)] = 1
            result += 1
        return str(x * (result - 1))

fin = open('A-large.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())
for i in range(t):
    print('Case #' + str(i + 1) + ': ' + answer(int(fin.readline())))
    
fout.close()
    