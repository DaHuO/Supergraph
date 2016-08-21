import random as rd

file_in = open("A-large.in", "r")
file_out = open("A-large.out", "w")

N = int(file_in.readline())
cnt = 0
for data in file_in:
    N = int(data)
    cnt += 1
    msg = "INSOMNIA"
    if N != 0:
        true_digits = 0
        digits = [False] * 10
        c = 0
        while true_digits < 10:
            c += 1
            n = c * N 
            while n > 0:
                r = n % 10
                n = n // 10
                if not digits[r]:
                    digits[r] = True
                    true_digits += 1
            msg = str(c * N)
    file_out.write("Case #" + str(cnt) + ": " + msg + "\n")

file_in.close()
file_out.close()
