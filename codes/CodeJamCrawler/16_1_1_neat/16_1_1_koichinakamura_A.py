def solve(S):
    answer = []
    for c in S:
        if all(c >= t for t in answer):
            answer.insert(0, c)
        else:
            answer.append(c)
    return ''.join(answer)

for c in range(input()):
    answer = solve(list(raw_input()))
    print 'Case #{}: {}'.format(c+1, answer)
