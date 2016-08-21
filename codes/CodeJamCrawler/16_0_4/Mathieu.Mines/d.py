def solve(numbers):
    if numbers[0] == numbers[2]:
        return ' '.join(map(str, range(1, 1+numbers[0])))
    return 'IMPOSSIBLE'

with open('input.txt') as f:
    data = f.readlines()

res = ""
N = int(data[0])
offset = 1
for i in range(N):
    x = map(int,data[i*offset+1].split())
    res += "Case #{}: {}\n".format(i+1, solve(x))

with open('output.txt','w') as f:
    f.write(res)


