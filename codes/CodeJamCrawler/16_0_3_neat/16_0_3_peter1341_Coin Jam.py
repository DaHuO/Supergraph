import sys

N=32
J=500
# J = 1
a = [0] * N
a[0] = 1
a[N - 1] = 1
data = [0] * 11
for i in range(2, 11):
    data[i] = [0] * N
    data[i][0] = 1
    for ii in range(1, N):
        data[i][ii] = data[i][ii - 1] * i
# print data
cnt = 0

divider_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
res = []
divider_res_save = []


# print data


def IsPrime():
    divider_res = []
    for i in range(2, 11):
        isprime = True
        tester = 0
        for ii in range(N):
            tester += a[ii] * data[i][ii]
        for divider in divider_list:
            if tester % divider == 0:
                # print tester, divider
                isprime = False
                divider_res.append(divider)
                break
        if isprime:
            return True, None
    return False, divider_res


def Update():
    for i in range(1, N):
        if a[i] == 0:
            a[i] = 1
            for j in range(1, i):
                a[j] = 0
            break


while res.__len__() < J:
    isprime, divider_res = IsPrime()
    if not isprime:
        res.append(list(a))
        divider_res_save.append(divider_res)
    Update()

for i in range(res.__len__()):
    # print res[i]
    _str = ""
    for ii in range(res[i].__len__() - 1, -1, -1):
        _str += str(res[i][ii])
    sys.stdout.write(_str)
    for divider in divider_res_save[i]:
        sys.stdout.write(' ' + str(divider))
    print ''

with open('output.txt', 'w') as f:
    f.write("Case #1:\n")
    for i in range(res.__len__()):
        # print res[i]
        _str = ""
        for ii in range(res[i].__len__() - 1, -1, -1):
            _str += str(res[i][ii])
        f.write(_str)
        for divider in divider_res_save[i]:
            f.write(' ' + str(divider))
        f.write('\n')
