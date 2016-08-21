def Cal(n, flip, tside):
    if done[n][flip][tside]:
        return dp[n][flip][tside]
    bot = s[n-1]^flip
    return min(
        (tside^bot)+Cal(n-1, flip^tside^bot, tside),
        Cal(n-1, flip, bot)+(tside^bot)
    )

for case in range(1, int(raw_input())+1):
    print "Case #%d: "%case, 
    s = raw_input().strip()
    assert all(map(lambda c: c in "+-", s))
    N = len(s)
    done = [[[False, False], [False, False]] for _ in range(N+1)]
    done[0] = [[True, True], [True, True]]
    dp = [[[0, 0], [0, 0]] for _ in range(N+1)]
    s = map(lambda c: c=='-', s)
    print Cal(N, False, False)
