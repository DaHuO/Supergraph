def flip(s):
    top_side = s[0]
    if (top_side=='-'):
        flip_to = '+'
    else:
        flip_to = '-'

    if flip_to in s :
        index = s.index(flip_to)
    else :
        index = len(s)

    s = flip_to*index+s[index:]
    return s

if __name__ == '__main__':
    inp = open("large_input.txt", "r")
    out = open("large_output.txt","w")
    test_cases = [x.strip('\n') for x in inp.readlines()]
    test_case_num = 1
    while test_case_num <= int(test_cases[0]):
        flips = 0
        stack = test_cases[test_case_num]
        while stack != '+'*len(stack):
            stack = flip(stack)
            flips += 1
        out.write('Case #{}: {}\n'.format(test_case_num,flips))
        test_case_num += 1

