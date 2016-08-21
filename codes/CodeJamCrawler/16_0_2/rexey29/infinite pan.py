file = open('input.in', 'r')
writef = open('output.txt', 'w')
def extension(p):
    ex = []
    for x in range(0, len(p)+1):
        new = []
        for x in range(x):
            if p[x] == '-':
                new.insert(0,'+')
            else:
                new.insert(0,'-')
        new.extend(p[x+1:])
        ex.append(new)
    return ex

def breadth_first_solve(puzzle):
    seen = [puzzle]
    def check_options(extension, seen):
        if extension in seen:
            return True
        else:
            seen.append(extension)
            return False
    queue = []
    queue.append({'p':puzzle, 'level': 0})
    while queue:
        node = queue.pop(0)
        if '-' not in node['p']:
            print(node['level'])
            return node['level']
        for x in extension(node['p']):
            if (not check_options(x, seen)) and len(x) == len(node['p']):
                queue.append({'p':x, 'level': node['level'] + 1})

cases = int(file.readline().strip())
for case in range(cases):
    s = list(file.readline().strip())
    a = breadth_first_solve(s)
    print("Case #{}: {}".format(case+1, a))
    writef.write("Case #{}: {}\n".format(case+1, a))
file.close()
writef.close()
