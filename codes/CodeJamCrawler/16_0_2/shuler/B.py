INPUT_FILE = "B-large.in"
OUTPUT_FILE = "B-large.out"
res = []

def write_output():
    out_file = open(OUTPUT_FILE, "w")
    for i,line in enumerate(res):
        out_file.write("Case #%d: %s\n" % (i+1, line))
    out_file.close()

def count_plusminus(stack):
    curr = stack[0]
    if len(stack) == 1:
        return 0
    res = 0
    for i in stack[1:]:
        if curr == '+' and i == '-':
            res += 1
        curr = i
    return res

def solve(case):
    plusminus = count_plusminus(case)
    first = case[0]
    if first == '+':
        return 2 * plusminus
    return 2 * plusminus + 1
    
def get_next(data):
    for line in data:
        case = line.strip()
        yield case

if __name__ == '__main__':
    print 'Starting...'
    f = file(INPUT_FILE)
    for line in get_next(f.read().strip().split('\n')[1:]):
        res.append(solve(line))
    write_output()
    f.close()
    print 'done.'