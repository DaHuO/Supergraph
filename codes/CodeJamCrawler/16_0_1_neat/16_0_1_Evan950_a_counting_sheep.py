def count_sheep(n):
    
    seen = {0: False,
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False,
            7: False,
            8: False,
            9: False}
    
    if n == 0:
        return "INSOMNIA"

    i = 1
    while False in seen.values():
        last = i*n
        for d in str(i*n):
            if not seen[int(d)]:
                seen[int(d)] = True
        i += 1

    return last

def read_data(filename):
    data = [int(line) for line in open(filename)]
    return (data.pop(0), data)

def write_data(filename, data):
    total, tests = data
    
    f = open(filename, 'w')

    for i,t in enumerate(tests):
        f.write("Case #{}: {}\n".format(i+1, count_sheep(t)))

if __name__ == "__main__":
    write_data("A-large.out", read_data("A-large.in"))
