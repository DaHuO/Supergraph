import sys

def find_last(number):
    all_previous = set("0123456789")
    i = 0
    if number == 0:
        return 'INSOMNIA'
    while all_previous:
        i += number
        all_previous -= set(str(i))
    return i

numtrials = int(sys.stdin.readline().strip())

for rep in range(numtrials):
    val = int(sys.stdin.readline().strip())
    print("Case #{}: {}".format(rep+1,find_last(val)))