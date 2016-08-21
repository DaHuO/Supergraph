
def main():
    fname = 'D-small-attempt0'
    with open(fname+'.in', 'r') as f:
        T, *indata = f.readlines()
    data = []
    for _ in indata:
        data.append([int(__) for __ in _.split()])

    results = [range(1, k+1, 1) for k,c,s in data]
    with open(fname+'.out', 'w') as f:
        for i, result in enumerate(results, 1):
            _ = ' '.join([str(_) for _ in result])
            print('Case #{}: {}'.format(i, _), file=f)

if __name__ == '__main__':
    main()
