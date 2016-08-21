digits = {'0', '1', '2', '3','4', '5', '6', '7', '8', '9'}
for test_case in range(int(input())):
    n = input()
    digits_seen = []
    insomnia = True
    for index in range(1,1000):
        digits_seen.extend([c for c in str(n * index) if c not in digits_seen])
        if set(digits_seen) == digits:
            print("Case #{}: {}".format(test_case + 1, index * n))
            insomnia = False
            break
    if insomnia: print("CASE #{}: INSOMNIA".format(test_case + 1))
