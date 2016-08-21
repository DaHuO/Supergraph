def count_sheep(sheep):
    sheep = int(sheep)
    if sheep == 0:
        return 'INSOMNIA'
    digits = set()
    all_digits = {'0','1','2','3','4','5','6','7','8','9'}
    i = 0
    while digits != all_digits:
        i += 1
        current_sheep = i*sheep
        digits.update(str(current_sheep))
    return current_sheep

def parse_sheep(file):
    numbers = list(map(int, file.readlines()))
    assert numbers[0] == len(numbers)-1
    results = []
    for i in range(1, len(numbers)):
        results.append('Case #{}: {}\n'.format(i, count_sheep(numbers[i])))
    map(print, results)
    return results

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        with open(sys.argv[2], 'w') as f2:
            f2.writelines(parse_sheep(f))