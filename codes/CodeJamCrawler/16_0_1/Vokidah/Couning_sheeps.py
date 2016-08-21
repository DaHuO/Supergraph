def check(N , set_of_numbers, count):
    #print(N)
    if N == 0:
        return "INSOMNIA"
    i = 1
    number = N
    while len(set_of_numbers) != 10:
        number = N * i
        for each in str(number):
            if each not in set_of_numbers:
                set_of_numbers.add(each)
        i += 1
    return number


T = int(input())
f = open('workfile', 'w')
for j in range(1, T + 1):
    n = int(input())
    f.write("Case #%s: %s\n" % (j, check(n, set([]), 2)))