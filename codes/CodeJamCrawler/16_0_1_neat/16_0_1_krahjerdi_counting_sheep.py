def compute(n, i=1, seen=[]):
    if n == 0:
        return 'INSOMNIA'
    for c in str(i * n):
        if c not in seen:
            seen.append(c)
    if len(seen) == 10:
        return i * n
    i += 1
    return compute(n, i=i, seen=seen)

with open("in.txt") as f:
    lines = [x.strip("\n") for x in f.readlines()]
    
test_case_count = lines.pop(0)

i = 1

for l in lines:
    print("Case #{}: {}".format(i, compute(int(l), i=1, seen=[])))
    i += 1