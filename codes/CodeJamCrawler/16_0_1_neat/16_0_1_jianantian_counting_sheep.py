
fr = open('A-large.in', 'r')
li = fr.readlines()
n = int(li[0])
t_list = li[1:]


def find_digit(x):
    digits = []
    while x:
        digits.append(x % 10)
        x /= 10
    return digits


def check(num):
    r = 10000
    che = 0
    total_digits = []
    for k in range(1, r):
        digits = find_digit(k * num)
        set_num = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        if set_num.issubset(set(total_digits)):
            res = (k - 1) * num
            che += 1
            break
        else:
            total_digits.extend(digits)

    if che == 0:
        res = 'INSOMNIA'
    return res

#print check(1692)


list_t = []
list_i = []
for i in range(n):
    t = int(t_list[i])
    list_i.append(i + 1)
    list_t.append(check(t))


out = open('A-large-out.out', 'w')
for j in range(n):
    out.write('Case #' + str(list_i[j]) + ': ' + str(list_t[j]) + '\n')
out.close()


