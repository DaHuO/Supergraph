def flip(pc):
    return ''.join(['+' if p == '-' else '-' for p in reversed(pc)])

def brute_force(pc, depth=0):
    if pc == '+' * len(pc): return 0
    if depth >= len(pc): return float('inf')

    best_result = float('inf')
    for i in range(1, len(pc) + 1):
        new_pc = flip(pc[:i]) + pc[i:]
        best_result = min(best_result, 1 + brute_force(new_pc, depth + 1))
    return best_result

def heuristic(pc):
    answer = 0
    for i in range(len(pc)):
        if i==0 or pc[i] != pc[i-1]:
            answer += 1
    if pc[-1] == '+':
        answer -= 1
    return answer

def generate(length):
    if length == 0:
        yield ''
    else:
        for el in generate(length - 1):
            yield '+' + el
            yield '-' + el

def test():
    for pc in generate(7):
        assert heuristic(pc) == brute_force(pc), "Not matching for %s" % (pc,)

if __name__ == '__main__':
    ncases = int(input())

    for case in range(1, ncases + 1):
        inpt = input().strip()
        print("Case #%d:" % (case,), heuristic(inpt))
