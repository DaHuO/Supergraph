t = int(input())  # number of test cases

l = list()
for i in range(t):
    l.append(int(input()))

for i in range(1, t+1):
    n = l[i-1]
    dig_set = set()
    if n == 0:
        r = "INSOMNIA"
    else:
        j = 1
        while len(dig_set) != 10:
            num = j * n
            no = num
            j += 1
            while num != 0:
                d = num % 10
                num /= 10
                dig_set.add(d)
        r = str(no)
    print "Case #{}: {}".format(i, r)

