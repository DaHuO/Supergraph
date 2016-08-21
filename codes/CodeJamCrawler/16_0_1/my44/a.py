t = int(raw_input())
lines = [0 for i in range(t)]
for i in range(t):
    lines[i] = int(raw_input())
ans = [None for i in range(t)]
for idx, num in enumerate(lines):
    if num == 0:
        ans[idx] = "INSOMNIA"
        continue
    N = 1
    not_seen_digit = range(10)
    while True:
        tmp_num = N*num
        numlist = map(int, list(str(tmp_num)))
        for i in numlist:
            if i in not_seen_digit:
                not_seen_digit.remove(i)
        if not not_seen_digit:
            break
        N += 1

    ans[idx] = N*num

for idx, num in enumerate(ans):
    outstr = "Case #{0}: {1}".format(idx+1, num)
    print(outstr)
