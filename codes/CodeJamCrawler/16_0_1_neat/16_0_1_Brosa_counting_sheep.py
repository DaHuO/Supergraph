t = int(input())

for i in range(t):
    print("Case #%d: " % (i + 1), end='')
    n = int(input())
    if n == 0:
        print("INSOMNIA")
        continue

    numbers = set()

    i = 1
    while True:
        numbers.update(list(map(int, list(str(i * n)))))
        if {0,1,2,3,4,5,6,7,8,9} <= numbers:
            break
        i += 1

    print(i * n)
