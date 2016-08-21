def verify(numbers):
    for i in range(0, len(numbers)):
        if not numbers[i]:
            return False
    return True

def set_existing(curr, numbers) :
    existing = str(curr)
    for c in existing:
        numbers[int(c)] = True

def solve(n) :
    if n == 0 :
        return "INSOMNIA"
    numbers = [False]*10
    curr = n
    while True:
        set_existing(curr, numbers)
        if verify(numbers):
            return str(curr)
        curr += n
    return "INSOMNIA"


cases = int(raw_input())
for i in range (1, cases+1):
    print "Case #" + str(i) + ": " + solve(int(raw_input()))
