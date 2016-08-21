num_str = [
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
]

def included_in_str(s, target):
    count = 0
    for ch in target:
        if ch in s:
            count += 1
            split_idx = s.find(ch)
            s = s[:split_idx] + s[split_idx + 1:]

    if count == len(target):
        return True
    else:
        return False

def solve(s, start=0):
    if s == '':
        return ''
    for n in range(10):
        # print('n=', n, 'start=', start, s)
        if included_in_str(s[:], num_str[n]):
            next_s = s[:]
            for ch in num_str[n]:
                # remove ch from s
                split_idx = next_s.find(ch)
                next_s = next_s[:split_idx] + next_s[split_idx + 1:]
            # print('removed {}: {}'.format(num_str[n], next_s))
            result_str = solve(next_s, start=n+1)
            if result_str is not None:
                return str(n) + result_str

T = int(input())
i = 0
for _ in range(T):
    i += 1
    s = input()
    print('Case #{}: {}'.format(i, solve(s)))
