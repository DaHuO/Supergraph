def main() -> None:
    outfile = open('cs_output.out', 'w')
    name = input()
    case = open(name, 'r')
    caselist = case.readlines()
    tests = int(caselist[0])
    count = 0
    for c in caselist[1:]:
        count += 1
        outfile.write('Case #{}: {}\n'.format(count, counting_sheep(int(c))))
    case.close()
    outfile.close()

def counting_sheep(N: int):
    check = set('0123456789')
    i = 1
    if N == 0:
        return "INSOMNIA"
    
    while ((check != set()) ):
        x = set(list(str( i * N )))
        check = check.difference(check.intersection(x))
    
        i += 1
    return (i-1) * N


main()

