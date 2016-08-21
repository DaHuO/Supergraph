tests = int(input())
t_nums = []
for t in range(tests):
    t_nums.append((t, int(input())))
for t_num in t_nums:
    t, num = t_num
    snum = num
    seen = set(list(str(snum)))
    prev_seen = set()
    for x in range(100):
        prev_seen = {s for s in seen}
        snum += num
        for d in list(str(snum)):
            seen.add(str(d))
        if all([x in seen for x in {'0','1','2','3','4','5','6','7','8','9'}]):
            ans = snum
            break
    else:
        ans = 'INSOMNIA'
    print('Case #{}: {}'.format(t + 1, ans))
