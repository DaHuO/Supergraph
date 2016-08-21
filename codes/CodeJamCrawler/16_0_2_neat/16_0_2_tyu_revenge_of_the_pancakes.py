input_file = "B-large.in"
output_file = "B-large.out"

def main():
    results = []
    
    f = open(input_file, 'r')
    T = int(f.readline())
    for t in range(T):
        stack = f.readline().strip()
        opt_flips = flip_pancakes(stack)
        results.append(opt_flips)
    f.close()

    f_out = open(output_file, 'w')
    for t in range(T):
        f_out.write('Case #%d: %d\n' % (t+1, results[t]))
    f_out.close()

def flip_pancakes(stack):
    flips = 0
    if stack[-1] == '-':
        flips = 1
    prev = stack[0]
    for i in range(1, len(stack)):
        if not stack[i] == prev:
            flips += 1
            prev = stack[i]
    return flips

if __name__ == "__main__":
    main()
