def sheep(n):
    def sheep_helper(n,dic):
        index = 1
        for iteration in range (len(str(n))):
            num = (n // (index)) % 10
            index *= 10
            dic[num] = 1
        return dic

    def sheep_primer(n, multiplier = 1, dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}):
        all_seen = True
        new_dic = sheep_helper(n, dic)
        number = n
        for element in new_dic:
            if not(new_dic[element] == 1):
                all_seen = False
        if not all_seen:
            if not(multiplier == 1):
                n = int((n/(multiplier - 1)) * multiplier)
            all_seen, number = sheep_primer(n, multiplier + 1, dic)
        return all_seen, number

    try:
        return_val = sheep_primer(n)[1]
    except:
        return_val = 'INSOMNIA'
    return return_val

if __name__ == '__main__':
    file = open('A-large.in.txt', 'r')
    line = 1
    case_number = 0
    for i in file:
        if line != 1:
            print('Case #' + str(case_number) + ': ' + str(sheep(int(i))))
        else:
            line += 1
        case_number += 1