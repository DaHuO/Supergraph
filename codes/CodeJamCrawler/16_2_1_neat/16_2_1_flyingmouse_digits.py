t = int(raw_input())  # read a line with a single integer
digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def translate(s, dic):
    res = ''
    index = 0
    while sum(dic.values()) != 0:
        if index > 9:
            while index > 9:
                index = int(res[-1]) + 1
                res = res[:-1]
                for x in digits[index-1]:
                    if x not in dic:
                        dic[x] = 1
                    else:
                        dic[x] += 1

        digit = digits[index]
        flag = True
        prev_dic = dic.copy()
        for x in digit:
            if x in dic and dic[x] > 0:
                dic[x] -= 1
            else:
                flag = False
                dic = prev_dic.copy()
                index += 1
                break
        if flag:
            res += str(index)
    return res


for i in xrange(1, t + 1):
    s = raw_input().lower()
    dic = {}
    for x in s:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
    print "Case #{}: {}".format(i, translate(s, dic))
