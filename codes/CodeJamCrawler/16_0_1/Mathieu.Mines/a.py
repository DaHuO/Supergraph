def solve(start):
    num_set = set()
    digit_set = set()
    num = start
    while num not in num_set:
        digit_set.update(set(str(num)))
        if len(digit_set) == 10:
            return num
        num_set.add(num)
        num += start
    return "INSOMNIA"

with open('input.txt') as f:
    data = f.readlines()

res = ""
N = int(data[0])
offset = 1
for i in range(N):
    x = int(data[i*offset+1])
    res += "Case #{}: {}\n".format(i+1, solve(x))

with open('output.txt','w') as f:
    f.write(res)


