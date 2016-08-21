for tc in range(1, int(input()) + 1):
    s = input()
    back = []
    front = [s[0]]
    for ch in s[1:]:
        if ch >= front[-1]:
            front.append(ch)
        else:
            back.append(ch)
    print('Case #{}: '.format(tc), *(front[i] for i in range(len(front) - 1, -1, -1)), *back, sep='')
