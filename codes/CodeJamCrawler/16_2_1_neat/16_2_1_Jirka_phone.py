
nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def function(line):
    line = list(line)
    tel = trying(line, 0)
    return ''.join(map(str,tel))

def trying(line, i):
    if line == []:
        return []
    if i>9:
        return None
    tel = []
    oldline = line
    newline = lookfor(oldline, nums[i])
    while oldline != newline:
        tel.append(i)
        t = trying(newline, i+1)
        if t is not None:
            return tel + t
        oldline = newline
        newline = lookfor(oldline, nums[i])
    return trying(line, i+1)

def lookfor(inp, num):
    line = list(inp)
    for letter in num:
        found = False
        for l in line:
            if letter == l:
                found = True
                line.remove(l)
                break
        if not found:
            return inp
    return line



# MAIN
# input like this:
# T
# n  ----> Case #1: m
# n  ----> Case #1: m
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()[1:]):
        print('Case #' + str(i+1) + ': ' + str(function(line[:-1])))


