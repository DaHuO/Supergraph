from read import read


def s(n):
    return chr(65+n)


def calc(N, st):
    ret = ''
    N = int(N)
    st = list(map(int, st.split()))
    p_sum = sum(st)
    # print(N, p_sum)
    if N==2:
        cnt = 0
        while (cnt < p_sum):
            if ret == '' and p_sum%2:
                ret += 'A ' if st[0] > st[1] else 'B '
                cnt += 1
                if st[0] > st[1]:
                    st[0] -= 1
                else:
                    st[1] -= 1
            if st[0] > st[1] and st[0] > 0:
                ret += 'A'
                st[0] -= 1
            else:
                ret += 'B'
                st[1] -= 1
            cnt += 1
            if cnt == p_sum:
                break
            if st[0] > st[1] and st[0] > 0:
                ret += 'A'
                st[0] -= 1
            else:
                ret += 'B'
                st[1] -= 1
            cnt += 1
            ret += ' '
    elif N==3:
        cnt = 0
        while (cnt < p_sum):
            if p_sum - cnt == 3:
                ret += 'A BC'
                break
            mx = max(st)
            if st[0] == mx and st[0] > 0:
                ret += 'A'
                st[0] -= 1
            elif st[1] == mx and st[1] > 0:
                ret += 'B'
                st[1] -= 1
            else:
                ret += 'C'
                st[2] -= 1
            cnt += 1
            if cnt == p_sum:
                break
            mx = max(st)
            if st[0] == mx:
                ret += 'A'
                st[0] -= 1
            elif st[1] == mx:
                ret += 'B'
                st[1] -= 1
            else:
                ret += 'C'
                st[2] -= 1
            cnt += 1
            ret += ' '
    return ret


# def calc(N, st):
#     ret = ''
#     st = list(map(int, st.split()))
#     p_sum = sum(st)
#     mx = max(st)
#     for _ in range(p_sum):
#         for idx,p in enumerate(st):
#             if p==mx:
#                 ret += s(idx)
#             st[idx] -= 1
#             mx = max(st)
#     return ret


def main():
    import sys
    infile = read(sys.argv[1])
    outfilename = sys.argv[2]
    def it():
        return next(infile)

    T = int(it())

    with open(outfilename, 'w') as outfile:
        for caseidx in range(1, T+1):
            N = it()
            ps = it()
            ans = calc(N, ps)
            outfile.write('Case #{}: {}\n'.format(caseidx, ans))
            print('Case #{}: {}'.format(caseidx, ans))


if __name__ == '__main__':
    main()
