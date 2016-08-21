def flip(n, state_list):
    temp = state_list[:n]
    for i in range(0, len(temp)):
        if temp[i] == '+':
            temp[i] = '-'
        else:
            temp[i] = '+'
    temp.reverse()
    return temp + state_list[n:]


t = int(input())
for i in range(1, t + 1):
    p = input()
    p_list = list(p)
    m = 0

    up = len(p_list)

    done = False

    while not done:
        if '-' not in p_list:
            print("Case #{}: {}".format(i, m))
            break

        if '+' not in p_list:
            p_list = flip(up, p_list)
            m += 1
            print("Case #{}: {}".format(i, m))
            break

        for j in range(up):
            for k in range(j, up):
                if p_list[j] != p_list[k]:
                    break

            p_list = flip(k, p_list)
            m += 1
            break
