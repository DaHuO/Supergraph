import math


def rec(i):
    global ctr
    if i == n:
        if arr[n-1] == 0:
            return
        if ctr == want:
            return

        for j in range(2, 11, 1):
            l = 1
            no = 0
            for k in range(31, -1, -1):
                no += arr[k]*l
                l *= j

            flag = 1
            for k in range(2, 1000, 1):
                if no % k == 0:
                    brr[j] = k
                    flag = 0
                    break

            if flag == 1:
                return

        for x in range(0, 32, 1):
            f1.write(str(arr[x]))

        f1.write(" ")
        for y in range(2, 11, 1):
            f1.write(str(brr[y]))
            f1.write(" ")

        f1.write("\n")
        ctr += 1
        return

    arr[i] = 1
    rec(i+1)
    if ctr == want:
        return

    arr[i] = 0
    rec(i+1)
    return


arr = {}
brr = {}
t = 1
n = 32
want = 500
ctr = 0
f1 = open('output.txt', 'w')
f1.write("Case #1:")
f1.write("\n")
rec(0)