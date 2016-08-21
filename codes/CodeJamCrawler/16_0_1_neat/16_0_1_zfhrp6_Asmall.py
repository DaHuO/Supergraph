from read import read

def calc(T):
    # print(T)
    if T == 0:
        return 'INSOMNIA'
    tmpT = str(T)
    nums = dict({(str(x), 0) for x in range(10)})
    i = 1
    while True:
        # print('\t', T)
        # print('\t\t', nums)
        for c in list(tmpT):
            nums[c] = 1
        if len(list(filter(lambda x:x==0, nums.values()))) == 0:
            return tmpT
        i += 1
        tmpT = str(i * int(T))


def main():
    # infile = read('A-small-attempt2.in')
    infile = read('A-large.in')
    def it():
        return next(infile)
    N = int(it())
    with open('A_large_output.txt', 'w') as outfile:
        for _ in range(N):
            num = it()
            ans = calc(int(num))
            outfile.write('Case #{}: {}'.format(_+1, ans))
            outfile.write('\n')
            print('{} -> Case #{}: {}'.format(num, _+1, ans))


if __name__ == '__main__':
    main()
