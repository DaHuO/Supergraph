SLEEP = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

def get_soln(in_num):
    if in_num == 0:
        return 'INSOMNIA'
    else:
        seen = set()
        num = in_num
        x = 2
        while True:
            seen.update(map(int, str(num)))
            if seen == SLEEP:
                break
            else:
                num = in_num * x
                x += 1

        return num


num_problems = int(input())
for i in range(num_problems):
    num = int(input())
    soln = get_soln(num)
    print('Case #{}: {}'.format(i + 1, soln))