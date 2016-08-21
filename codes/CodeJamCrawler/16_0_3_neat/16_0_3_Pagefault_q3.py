import primesieve

def solve(start, end, required_results):
    primes = primesieve.generate_n_primes(0x10000)
    results = []
    x = start # 0b10000000000000000000000000000001
    while x < end: # 0b100000000000000000000000000000000:
        deviders = []
        str_x = bin(x)[2:]
        for b in range(2,11):
            x_in_base = int(str_x, b)
            half_x = x_in_base >> 1
            devider = 1
            for p in primes:
                if p > half_x:
                    break
                if 0 == x_in_base % p:
                    devider = p
                    break
            if 1 == devider:
                break
            deviders.append(devider)
        else:
            results.append("%s %s" % (str_x, ' '.join([str(devider) for devider in deviders]).strip()))
            if len(results) >= required_results:
                break
        x += 2
    return results

def write_results_to_file(results, file_name):
    out_file = open(file_name, 'wb')
    out_file.write('Case #1:\n')
    for l in results:
        out_file.write(l + '\n')
    out_file.close()

small_set = solve(int('1' + ('0' * 13) + '11', 2), int('1' + ('0' * 16), 2), 50)
large_set = solve(int('1' + ('0' * 29) + '11', 2), int('1' + ('0' * 32), 2), 500)

write_results_to_file(small_set, 'small.out')
write_results_to_file(large_set, 'large.out')
