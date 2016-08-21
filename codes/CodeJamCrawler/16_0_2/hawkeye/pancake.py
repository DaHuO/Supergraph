def doer(S):
    if S.find('+')==-1:
        return 1
    if S.find('-')==-1:
        return 0

    S_list = S.split('+')
    S_list.sort(reverse=True)
    #checking first position of '+'
    num_begin = S.find('+')
    if '' in S_list:
        num_all = S_list.index('')
    else:
        num_all = len(S_list)
    if num_begin == 0:
        total = num_all*2
    else:
        total = 1 + (num_all-1)*2
    return total

if __name__ == '__main__':
    T = input()
    for i in range(T):
        print 'Case #{0}: {1}'.format(i+1, doer(raw_input()))
