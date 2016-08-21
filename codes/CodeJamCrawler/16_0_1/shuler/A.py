INPUT_FILE = "A-large.in"
OUTPUT_FILE = "A-large.out"
res = []

def write_output():
    out_file = open(OUTPUT_FILE, "w")
    for i,line in enumerate(res):
        out_file.write("Case #%d: %s\n" % (i+1, line))
    out_file.close()

def update_set(s,num):
    while num > 0:
        s.add(num % 10)
        num = num / 10

def solve(case):
    n = int(case)
    if n == 0:
        return "INSOMNIA"
    s = set()
    total = n
    while True:
        update_set(s,total)
        if len(s) == 10:
            break
        total += n
    return total
    
def get_next(data):
    for line in data:
        case = line.strip()
        yield case

if __name__ == '__main__':
    print 'Starting...'
    f = file(INPUT_FILE)
    for line in get_next(f.read().split('\n')[1:]):
        res.append(solve(line))
    write_output()
    f.close()
    print 'done.'