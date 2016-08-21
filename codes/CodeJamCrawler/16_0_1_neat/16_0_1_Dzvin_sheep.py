t = int(input())
lst = []
for i in range(t):
    n = int(input())
    lst.append(n)


def main(n):
    if n == 0:
        return 'INSOMNIA'
    lst_numbers = []
    new_n = n
    while len(lst_numbers) != 10:
        for num in str(new_n):
            if int(num) not in lst_numbers:
                lst_numbers.append(int(num))
        new_n += n
    return new_n - n

i = 1
for n in lst:
    print('Case #' + str(i) + ': ' + str(main(n)))
    i += 1



