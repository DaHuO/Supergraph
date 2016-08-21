# Read problem
no_of_cases = int(raw_input())
cases = []
for _ in range(no_of_cases):
    _n, _j = [int(number) for number in raw_input().split(' ')]
    cases.append((_n, _j))

# Iterate over cases
for i, case in enumerate(cases):
    n, j = case

    # Calculate decimal limits of the case
    min_limit = int('1' + '0' * (n-2) + '1', 2)
    max_limit = int('1' * n, 2)

    # For each decimal number between limits, with step 2 to meet restriction of
    # binary representation starting and ending with 1.
    print 'Case #{}:'.format(i+1)
    jamcoins_found = 0
    for k in xrange(min_limit, max_limit+1, 2):
        # Get binary representation
        binary_repr = bin(k)[2:]

        # Assume binary value is valid for now and initialize divisors array
        is_valid = True
        divisors = [0 for _ in range(9)]
        # Check every base (2-10) decimal interpretation
        for base in range(2, 11):
            decimal_interpretation = int(binary_repr, base)

            is_prime = True
            # Try to find some divisor. We must put a low limit to assure it
            # doesn't take too much checking the primality of high values.
            for l in xrange(2, 100):
                if decimal_interpretation % l == 0:
                    divisors[base-2] = str(l)
                    is_prime = False
                    break

            if is_prime:
                # This binary number is not a valid coin as far as we've
                # checked (could as well be a valid coin if we continue
                # trying more divisors)
                is_valid = False
                break

        if not is_valid:
            # Check next binary number
            continue
        else:
            # Print the solution and update counter
            print '{} {}'.format(binary_repr, ' '.join(divisors))
            jamcoins_found += 1
            if jamcoins_found == j:
                break
