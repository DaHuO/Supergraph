import sys

if __name__ == "__main__":
    _in = open("A_l.in", "r")
    _out = open("A_l.out", "w")
    T = int(_in.readline())
    for i in range(T):
        original = int(_in.readline()[:-1])
        n = original
        count = 0

        if (n == 0):
            ans = "INSOMNIA"
        else:
            check = set()

            while (n % 10 == 0):
                check.add(0)
                n = n // 10

            while (len(check) < 10):
                count += 1
                temp = n * count
                while (temp > 0):
                    check.add(temp % 10)
                    temp = temp // 10
            ans = count * original

        _out.write("Case #" + str(i+1) + ": " + str(ans) +"\n")
