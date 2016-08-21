def fnc(num, orig, i, visited=[]):
    if i > 1000:
        return "INSOMNIA"
    num += orig
    visited.extend(str(num))
    if len(set(visited)) == 10:
        return str(num)
    i += 1
    try:
        return fnc(num, orig, i, visited)
    except RecursionError:
        return "INSOMNIA"

count = input()
for i in range(int(count)):
    num = int(input())
    visited = list(str(num))
    print("Case #%d: %s" % (i+1,fnc(num, num, 1, visited)))
