import sys

def input_parser(input_path):
    with open(input_path, 'r') as f:
        c = int(f.readline())
        for case in range(c):
            n, j = list(map(int, f.readline().split()))
            yield case, (n, j)

def get_output_path(input_path):
    return input_path[:-2] + "out"

def output(f, s):
    print(s)
    f.write(s + "\n")

def all_numbers(n):
    out = [0]*n
    processed_num = 0
    yield out,[],[]
    while processed_num < pow(2,n)-1:
        added = []
        removed = []
        for i in range(n):
            if out[n-i-1] == 0:
                out[n-i-1] = 1
                added.append(i+1)
                break
            else:
                out[n-i-1] = 0
                removed.append(i+1)
        processed_num += 1 
        yield out, added, removed

CACHE = {}

def is_prime(n):
    if n in CACHE: 
        return CACHE[n]
    i = 2
    while i*i <= n and i!=0 and i!= n and i < 10000:
        if i in CACHE and not CACHE[i]:
            i += 1
            continue
        if n % i == 0:
            CACHE[n] = (False, i)
            return False, i
        i += 1
    CACHE[n] = (True, 0)
    return True, 0

def problem(g, n,j):
    bases = [] 
    for base in range(2, 11):
        multiples = [1]
        for multiple in range(1, n):
            multiples.append(base*multiples[-1])
        bases.append(multiples)
        print(base, multiples)

    base_numbers = []
    for base in bases:
        base_numbers.append(base[0] + base[n-1])

    output_list = []
    print(base_numbers)
    for num, added, removed in all_numbers(n-2):
        out = ['1' + ''.join(map(str,num)) + '1']
        print()
        print(out[0],added,removed)
        valid = True
        for ind, base in enumerate(bases):
            if len(added) > 0:
                base_numbers[ind] += base[added[0]]
            if len(removed) > 0:
                for r in removed:
                    base_numbers[ind] -= base[r]
            if valid:
                prime, div = is_prime(base_numbers[ind])
                print(base_numbers[ind], prime, div)
                if prime:
                    valid = False
                else:
                    out.append(div)

        if valid:
            output_list.append(out)
            if len(output_list) == j:
                output(g, "Case #1:")
                for o in output_list:
                    output(g, ' '.join(map(str, o)))
                return

def main():
    input_path = sys.argv[1]
    with open(get_output_path(input_path), 'w') as g:
        for case, data in input_parser(input_path):
            out = problem(g, *data)

if __name__ == "__main__":
    main()

