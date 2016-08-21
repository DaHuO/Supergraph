def read_data(filename):
    with open(filename) as f:
        cases = int(f.readline().strip())
        data = []
        for i in xrange(cases):
            number = f.readline().strip()
            data.append(number)
        return data

def count_sheeps(data):
    case = 0
    for number in data:
        case += 1
        digits = [False] * 10

        if number == '0':
            print 'Case #{}: INSOMNIA'.format(case)
        else:
            val_number = int(number)
            steps = 1
            found = False
            while not found:
                str_num = str(val_number)
                for d in str_num:
                    digits[int(d)] = True
                found = all(digits)
                if not found:
                    steps += 1
                    val_number = int(number) * (steps)
            print 'Case #{}: {}'.format(case, val_number)

if __name__ == '__main__':
    count_sheeps(read_data('A-large.in'))
