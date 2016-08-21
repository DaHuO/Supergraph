def main():
    file = open('in.txt', 'r')
    data = file.read()
    file.close()

    lines = data.split("\n")
    n = int(lines[0])
    result = ''
    for i in range(1, n + 1):
        s = lines[i]
        ret = solve(s)
        result += 'Case #' + str(i) + ': ' + ret + "\n"

    file = open('out.txt', 'w')
    file.write(result)
    file.close()


def solve(s):
    s = minify(s)
    prev = -1
    count = 0
    for i in range(len(s)):
        if s[i] == '+':
            prev = i
            continue
        if s[i] == '-':
            if prev != -1:
                if s[prev] == '+':
                    count += 2
            else:
                count += 1
    return str(count)

def minify(s):
    ret = s[0]
    count = 0
    for i in range(len(s)):
        if s[i] == ret[count]:
            continue
        ret += s[i]
        count += 1
    return ret

main()