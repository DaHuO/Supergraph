t = int(input())

for i in range(1, t+1):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    n = int(input())
    if n != 0:
        for m in range(n, 100 * n, n):
            for digit in str(m):
                if digit in digits:
                    digits.remove(digit)

            if not digits:
                print("Case #{}: {}".format(i,m))
                break
    if digits:
        print("Case #{}: INSOMNIA".format(i))
