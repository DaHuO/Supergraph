memo = {}

def solve(p):
    
    def flip(s):
        ns = []
        for c in s:
            if c == '+': ns.append('-')
            else: ns.append('+')
        return ''.join(ns)

    def evaluate(s):
        for c in s:
            if c != '+':
                return False
        return True

    q = [p]
    steps = [0]
    next = []
    visited = set([p])

    while q:
        # print q.__str__()
        stack = q.pop(0)
        step = steps.pop(0)

        if evaluate(stack):
            memo[stack] = step
            return step

        for i in range(len(stack)):
            top = stack[:i + 1]
            bottom = stack[i + 1:]
            top = flip(top)

            new_stack = top + bottom

            # if memo.get(new_stack, False): return step + memo[new_stack]
            
            if not new_stack in visited:
                q.append(new_stack)
                steps.append(step + 1)
                visited.add(new_stack)
                
    return -1

if __name__ == "__main__":
    FILENAME = 'B-small-attempt1.in'
    lines = open(FILENAME, 'r').read().split('\n')
    T = int(lines[0])

    for case in range(1, T+1):
        data = lines[case]

        answer = solve(data)
        print "Case #{0}: {1}".format(case, answer)
