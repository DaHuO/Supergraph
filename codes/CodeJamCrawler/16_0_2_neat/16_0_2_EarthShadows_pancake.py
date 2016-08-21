
f = open("B-large.in")
out = open("out.txt", "w")
T = int(f.readline())
print(T)

for i in range(T):
    str = f.readline().strip()
    print(str)
    expected = '+'
    count = 0
    for char in reversed(str):
        if char is not expected:
            count += 1
            expected = '+' if expected == '-' else '-'
    print("Case #{0}: {1}".format(i+1, count))
    out.write("Case #{0}: {1}\n".format(i + 1, count))