def get_digits(num):
    digit = []
    while num != 0:
        digit.append(num%10)
        num = num // 10
    return digit



if __name__ == '__main__':
    inp = open("large_input.txt", "r")
    out = open("large_output.txt","w")
    test_cases = [x.strip('\n') for x in inp.readlines()]
    test_case_num = 1
    digits = set()
    digits.update([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    while test_case_num <= int(test_cases[0]):
        N = int(test_cases[test_case_num])
        digits_seen = set()
        j = 1
        while digits_seen != digits and N != 0:
            digits_seen.update(get_digits(N*j))
            j += 1
        if N == 0:
            out.write('Case #{}: INSOMNIA\n'.format(test_case_num))
        else :
            out.write('Case #{}: {}\n'.format(test_case_num,N*(j-1)))
        test_case_num += 1



