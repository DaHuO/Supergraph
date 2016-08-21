T = int(input())

def alg(S):
    d = {chr(ord('A') + x):0 for x in range(26)}
    result = {x: 0 for x in range(10)}
    for C in list(S):
        d[C] += 1

    order_letters = ['W', 'X', 'Z', 'U', 'G', 'H', 'F', 'V', 'O', 'I']
    ordered_names = ['TWO', 'SIX', 'ZERO', 'FOUR', 'EIGHT', 'THREE', 'FIVE', 'SEVEN', 'ONE', 'NINE']
    ordered_digits = [2, 6, 0, 4, 8, 3, 5, 7, 1, 9]

    for i, letter in enumerate(order_letters):
        # W -> 2
        nb_occ = d[letter]
        result[ordered_digits[i]] += nb_occ
        for letter in list(ordered_names[i]):
            d[letter] -= nb_occ
    #
    # # W -> 2
    # nb_occ = d['W']
    # result[2] += nb_occ
    # for letter in list('TWO'):
    #     d[letter] -= nb_occ

    final_result = ""
    for digit in result.keys():
        final_result += str(digit) * result[digit]

    return(final_result)

for t in range(T):
    S = input()
    print('Case #{}: {}'.format(t + 1, alg(S)))
