num = int(input())

for n in range(1, num + 1):
    i = int(input())

    seen = {}
    finished = False

    if i == 0:
        print("Case #" + str(n) + ": INSOMNIA")
        continue

    z = 1
    while finished is False:
        num = str(i * z)
        for char in num:
            seen[char] = True

        finished = True
        for k in range(0, 10):
            if(str(k) in seen and seen[str(k)] is True):
                finished = finished and True
            else:
                finished = False

        if(finished):
            print("Case #" + str(n) + ": " + num)
        z += 1
