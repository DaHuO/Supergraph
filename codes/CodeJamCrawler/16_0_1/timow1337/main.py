t_max = int(input())

for t in range(t_max):
    N = int(input())
    x  = "INSOMNIA"
    if N != 0:
        digits = set()
        cur = N
        while len(digits) != 10:
            n = cur
            while n != 0: 
                digit = n % 10
                digits.add(digit)
                n = n // 10
            cur += N
        x = cur - N
    print("Case #" + str(t+1) + ": " + str(x))
