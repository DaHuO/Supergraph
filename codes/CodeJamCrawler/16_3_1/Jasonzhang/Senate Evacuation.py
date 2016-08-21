def evacuation(party_num, senate_num, total_num):
    result = ''
    while True:
        if total_num == 0:
            break
        result += (chr(senate_num.index(max(senate_num)) + ord('A')))
        senate_num[senate_num.index(max(senate_num))] -= 1
        total_num -= 1
        if senate_num[senate_num.index(max(senate_num))] >= (total_num / 2 + 1):
            result += (chr(senate_num.index(max(senate_num)) + ord('A')))
            total_num -= 1
            senate_num[senate_num.index(max(senate_num))] -= 1
        result += ' '
    return result


if __name__ == '__main__':
    # party_num = 2
    # senate_num = [2, 2]
    # total_num = 4
    # print evacuation(party_num, senate_num, total_num).strip()
    f = open('1.in')
    f1 = open('A.out', 'wb')
    T = int(f.readline().strip())

    for i in range(T):
        N = int(f.readline().strip())
        senate_num = f.readline().strip().split(' ')
        senate_num = [int(x) for x in senate_num]
        total = 0
        for j in senate_num:
            total += int(j)
        f1.write('Case #' + str(i + 1) + ': ' + evacuation(N, senate_num, total).strip() + '\n')

    f.close()
    f1.close()
