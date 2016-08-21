cases = int(raw_input())

for c in range(0, cases):
    n = int(raw_input())
    if n == 0:
        print("Case #"+str(c+1)+": INSOMNIA")
    else:
        counted = []
        num = 0
        current = ""

        while len(counted)< 10:
            num += 1
            current = str(num*n)

            for char in current:
                if char not in counted:
                    counted.append(char)

        print("Case #"+str(c+1)+": "+current)