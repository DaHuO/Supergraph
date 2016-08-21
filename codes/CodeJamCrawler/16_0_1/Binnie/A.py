import sys


def get_final_number(N):
    numbers_seen = [False] * 10
    num_so_far = 0
    multiplier = 1
    while True:
        num = N * multiplier
        fill_in_numbers(num, numbers_seen)
        if all_numbers_seen(numbers_seen):
            return num
        multiplier += 1

def all_numbers_seen(array):
    for ii in range(10):
        if not array[ii]:
            return False
    return True

def fill_in_numbers(N, array):
    as_string = str(N)
    for let in as_string:
        digit = int(let)
        array[digit] = True


f = open(sys.argv[1])
T = int(f.readline())
for test in range(T):
    N = int(f.readline())

    print "Case #%d: " % (test + 1), "INSOMNIA" if N == 0 else get_final_number(N) 
