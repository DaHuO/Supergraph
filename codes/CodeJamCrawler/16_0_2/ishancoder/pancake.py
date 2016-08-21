def flip(i, stack):
    first_half = stack[0:i+1]
    second_half = stack[i+1:]
    first_half.reverse()
    for i in range(len(first_half)):
        first_half[i] = not first_half[i]
    return first_half + second_half


def generate_possibilities(stack):
    possible = []
    for x in range(0, len(stack) + 1):
        ans = flip(x, stack)
        possible.append(ans)
    return possible


def convert_to_boolean(string):
    l = []
    for x in string:
        if x == "+":
            l.append(True)
        else:
            l.append(False)
    return l


def find_last_blank(stack):
    return len(stack) - 1 - stack[::-1].index(False)


def find_min_flip(stack):
    min_flip = 0
    while not all(stack):
        i = find_last_blank(stack)
        _stack = flip(i, stack)
        while _stack == stack:
            i -= 1
            _stack = flip(i, stack)
        min_flip += 1
        stack = _stack
    return min_flip


def bfs(stack, queue=[], visited=[], parent={}):
    parent[str(stack)] = None
    if all(stack):
        return parent
    else:
        possible = generate_possibilities(stack)
        queue.extend(possible + [stack])
        visited.extend(possible + [stack])
        for each in possible:
            if each != stack:
                parent[str(each)] = str(stack)
        while queue:
            x = queue.pop(0)
            if all(x):
                return parent
            else:
                possible = generate_possibilities(x)
                for each in possible:
                    if each not in visited:
                        queue.append(each)
                        parent[str(each)] = str(x)
                        visited.append(each)


def find_path(p, t):
    stack = str(t)
    l = []
    while p[stack] != None:
        l.append(stack)
        stack = p[stack]
    return l

N = int(input())
for _ in range(N):
    s = input()
    st = convert_to_boolean(s)
    truthy = [True for _ in range(len(st))]
    parent = bfs(st, queue=[], visited=[])
    ans = len(find_path(parent, truthy))
    print("Case #"+str(_+1)+": " + str(ans))

