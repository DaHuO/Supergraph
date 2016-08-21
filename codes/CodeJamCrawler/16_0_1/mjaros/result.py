count = int(input())
numbers = []
for k in range(count):
    numbers.append(int(input()))

for u in range(len(numbers)):
    found = []
    round_ = 1
    last_r = None
    print("Case #{0}:".format( u+1), end=' ')
    while found != 10:
        k = numbers[u] * round_
        l = k 
        while l > 0:
            if l % 10 not in found:
                found.append(l % 10)
            l = l // 10
        if k == last_r:
            print("INSOMNIA")
            break
        if len(found) == 10:
            print(k)
            break
        last_r = k * round_
        round_ += 1
        



