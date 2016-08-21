Q = int(input())

for qu in range(1, Q+1):
    n = int(input())
    if n == 0:
        print("Case #{}: INSOMNIA".format(qu))
    else:
        all_digit = {}
        num = 0
        while sum(all_digit.values()) < 10:
            num += n
            m = num
            while m:
                if m%10 not in all_digit:
                    all_digit[m%10] = 1
                m //= 10
        print("Case #{}: {}".format(qu,num))
