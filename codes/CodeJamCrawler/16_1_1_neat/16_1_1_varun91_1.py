def solve(string):
    chars = []

    for char in string:
        if "".join(chars)+char > char+"".join(chars):
            chars.append(char)
        else:
            chars.insert(0, char)
    return "".join(chars)

count = int(input())
for i in range(count):
    print("Case #%d: %s" % (i+1,solve(input())))
