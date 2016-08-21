T = int(raw_input())

for case in range(T):
    N = int(raw_input())
    odd = []
    all_numbers = {}
    for paper_index in range((2*N) -1):
        heights = map(int, raw_input().strip().split())
        for height in heights:
            if height in all_numbers:
                all_numbers[height] += 1
            else:
                all_numbers[height] = 1
    for height in all_numbers:
        if all_numbers[height] % 2 == 1:
            odd.append(height)
    print "Case #{}: {}".format(case+1, " ".join(map(str, sorted(odd))))

