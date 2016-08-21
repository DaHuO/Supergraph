N = 32
J = 500
top = 2**(N-1)
count = 0

print("Case #1:")
for i in range(0, 2**(N-16)):
    current = i*2 + top + 1
    binary = str(int(bin(current)[2:], 10))
    dividers = []
    
    for base in range(2, 11):
        converted = int(binary, base)
        for j in range(2, 100):
            if converted % j == 0:
                dividers.append(j)
                break
        else:
            break
    else:
        print(binary + " " + " ".join(str(x) for x in dividers))
        count = count + 1
        if count == J:
            break
