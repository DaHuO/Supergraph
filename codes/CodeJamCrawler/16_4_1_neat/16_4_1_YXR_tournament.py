

def get2min(x):
    tmp = 2
    while tmp <= x:
        tmp = tmp*2
    return tmp/2


def test(N, R, P, S, target):
    length = 2**N
    if R + P + S != length:
        return 'IMPOSSIBLE'
    ans = ''
    if target == 'R':
        ans += 'R'
        R -= 1
        if R < 0:
            return 'IMPOSSIBLE'
    elif target == 'P':
        ans += 'P'
        P -= 1
        if P < 0:
            return 'IMPOSSIBLE'
    elif target == 'S':
        ans += 'S'
        S -= 1
        if S < 0:
            return 'IMPOSSIBLE'
    while len(ans) != length:
        tmpl = len(ans)
        if tmpl%2 != 0:
            if ans[-1] == 'R':
                ans += 'S'
                S -= 1
                if S < 0:
                    return 'IMPOSSIBLE'
            elif ans[-1] == 'P':
                ans += 'R'
                R -= 1
                if R < 0:
                    return 'IMPOSSIBLE'
            elif ans[-1] == 'S':
                ans += 'P'
                P -= 1
                if P < 0:
                    return 'IMPOSSIBLE'
        else:
            min2 = get2min(tmpl)
            if min2 == tmpl:
                if ans[0] == 'R':
                    ans += 'S'
                    S -= 1
                    if S < 0:
                        return 'IMPOSSIBLE'
                elif ans[0] == 'P':
                    ans += 'R'
                    R -= 1
                    if R < 0:
                        return 'IMPOSSIBLE'
                elif ans[0] == 'S':
                    ans += 'P'
                    P -= 1
                    if P < 0:
                        return 'IMPOSSIBLE'
            else:
                if ans[min2] == 'R':
                    ans += 'S'
                    S -= 1
                    if S < 0:
                        return 'IMPOSSIBLE'
                elif ans[min2] == 'P':
                    ans += 'R'
                    R -= 1
                    if R < 0:
                        return 'IMPOSSIBLE'
                elif ans[min2] == 'S':
                    ans += 'P'
                    P -= 1
                    if P < 0:
                        return 'IMPOSSIBLE'
    return ans


def alpha(ans):
    if ans == 'IMPOSSIBLE':
        return ans
    tmp = ''
    length = len(ans)
    if length == 2:
        if ans[0] < ans[1]:
            return ans
        else:
            return ans[1] + ans[0]
    str1 = ans[0:len(ans)/2]
    str2 = ans[len(ans)/2:len(ans)]
    str1 = alpha(str1)
    str2 = alpha(str2)
    if str1 < str2:
        return str1 + str2
    else:
        return str2 + str1


def findans(N, R, P, S):
    str1 = alpha(test(N, R, P, S, 'R'))
    str2 = alpha(test(N, R, P, S, 'P'))
    str3 = alpha(test(N, R, P, S, 'S'))
    valid = []
    if str1 != 'IMPOSSIBLE':
        valid.append(str1)
    if str2 != 'IMPOSSIBLE':
        valid.append(str2)
    if str3 != 'IMPOSSIBLE':
        valid.append(str3)
    if valid == []:
        return 'IMPOSSIBLE'
    else:
        min0 = valid[0][0]
        minn = 0
        for i in range(len(valid)):
            string = valid[i]
            if string[0] < min0:
                min0 = string[0]
                minn = i
        return valid[minn]




f = open("a.txt")

lines = f.readlines()

T = int(lines[0])

cnt = 0
anslines = []
ansf = open('b.txt', 'w')
for line in lines[1:]:
    cnt += 1
    line = line.split(' ')
    N = int(line[0])
    R = int(line[1])
    P = int(line[2])
    S = int(line[3])

    ansstr = 'Case #' + str(cnt) + ': ' + findans(N, R, P, S)
    print >> ansf, ansstr


# print findans(3, 8, 0, 0)
# test(3, 8, 0, 0, 'R')
