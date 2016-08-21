import os
import sys


def compute_sleep(N):
    mul = 2
    temp_n = N
    not_seen = [x for x in range (0,10)]
    while True:
        old_n = temp_n
        while temp_n != 0:
            dig = temp_n % 10
            if dig in not_seen:
                not_seen.remove(dig)
            temp_n = temp_n / 10
        if not_seen == []:
            return old_n
        temp_n = mul * N
        mul = mul + 1
        if old_n == temp_n:
            return "INSOMNIA"

def sheep_sleeps(inp):
    op = open("output.txt","w")
    ip = open(inp)
    file_inp = ip.read().splitlines()
    test_cases = int(file_inp[0])
    for case in range(1,test_cases+1):
        final_number = compute_sleep(int(file_inp[case]))
        op.write("Case #%s: %s\n" % (case, final_number))
    op.close()
    ip.close()


if __name__ == '__main__':
    sheep_sleeps(sys.argv[1])

