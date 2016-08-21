import argparse



def sheepcount(n):
    n = int(n)
    if n == 0:
        return 'INSOMNIA'
    seen = []
    i = 1
    while(True):
        curr = i*n
        curr_str = str(curr)
        for digit in curr_str:
            if digit not in seen:
                seen.append(digit)
        if len(seen) == 10:
            return curr
        i += 1

def main():
    parser = argparse.ArgumentParser(description='Sheep Problem')
    parser.add_argument('filename', metavar='S', type=str)
    args = parser.parse_args()
    infile = open(args.filename, 'r')
    outfile = open('sheep_out.txt', 'w')

    T = infile.readline()
    for i in range(int(T)):
        N = infile.readline()
        outfile.write('Case #{0}: {1}\n'.format(i+1, sheepcount(N)))

if __name__ == '__main__':
    main()
                           

