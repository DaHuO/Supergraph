def counting_sheep(filename):
    file = open(filename, 'r')
    source = file.read()
    lines = source.splitlines()
    file.close()
    file = open('counting-sheep.txt', 'w')
    T = int(lines[0])
    for i in range(T):
        file.write('Case #' + str(i+1) + ': ')
        file.write(str(final_count(int(lines[i+1]))) + '\n')
    file.close()

def final_count(number):
    if number == 0:
        return 'INSOMNIA'
    digits = [False, False, False, False, False, False, False, False, False, False]
    count = 0
    while not all(digits):
        count += number
        for num in str(count):
            digits[int(num)] = True
    return count

counting_sheep('A-large.in')
