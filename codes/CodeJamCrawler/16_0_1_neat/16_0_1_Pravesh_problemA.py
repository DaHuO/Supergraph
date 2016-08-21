__author__ = 'pravesh'

file = open("A-large.in", "r").readlines()
T = int(file.pop(0))
i = 1

result = set("0123456789")

def get_count(N):
    seen = set()
    for i in range(200):
        num = N * (i+1)
        num_set = set(str(num))
        seen = seen.union(num_set)
        if seen == result:
            return num
    return "INSOMNIA"


while i <= T:
    N = int(file.pop(0))
    print("Case #%d:" % i, get_count(N))
    i += 1
