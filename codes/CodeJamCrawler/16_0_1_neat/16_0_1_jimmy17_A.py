tests = int(raw_input())

def solve(N):
    numbers = dict()
    count = 0
    for i in range(10):
        numbers[i] = False

    prod = 1
    if N == 0:
        return 'INSOMNIA'
    while True:
        current = prod * N
        while current > 0:
            digit = current % 10
            if numbers[digit] == False:
                count += 1
                if count == 10:
                    return prod * N
                numbers[digit] = True
            current = current / 10
        prod += 1

for i in range(tests):
    result = 0
    result = solve(int(raw_input()))
    print 'Case #'+ str(i+1)+': '+ str(result)
