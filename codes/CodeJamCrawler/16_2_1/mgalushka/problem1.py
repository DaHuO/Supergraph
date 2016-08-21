from sets import Set

def is_ok(_map):
    for _k, v in _map.iteritems():
        if v > 0:
            return False
    return True

if __name__ == "__main__":
    letters = {
        0: 'ZERO',
        1: 'ONE',
        2: 'TWO',
        3: 'THREE',
        4: 'FOUR',
        5: 'FIVE',
        6: 'SIX',
        7: 'SEVEN',
        8: 'EIGHT',
        9: 'NINE',
    }
    mapping = {
        'Z': 0,
        'W': 2,
        'U': 4,
        'X': 6,
        'G': 8,
    }
    mapping_2 = {
        'O': 1,
        'R': 3,
        'F': 5,
        'S': 7,
    }
    mapping_3 = {
        'N': 9,
    }

    data = []
    T = 0
    with open('/Users/mgalushka/google_code_jam/round1b/output1.out', 'w') as out:
        with open('/Users/mgalushka/google_code_jam/round1b/input1.in', 'r') as inp:
            T = int(inp.readline().strip())
            for case_number in range(1, T+1):
                word = inp.readline().strip()
                used = set(range(0, 10))
                result = []
                mapped_input = {}
                for letter in word:
                    if letter not in mapped_input:
                        mapped_input[letter] = 1
                    else:
                        mapped_input[letter] += 1

                for known, number in mapping.iteritems():
                    current_number = number
                    if known in mapped_input and mapped_input[known] > 0:
                        print(number)
                        while mapped_input[known] > 0:
                            for l in letters[number]:
                                print(mapped_input)
                                mapped_input[l] -= 1
                            result.append(number)
                    used.remove(number)
                print(mapped_input)
                print(is_ok(mapped_input))
                if is_ok(mapped_input):
                    result.sort()
                else:
                    print('2nd round')
                    # other numbers
                    for known, number in mapping_2.iteritems():
                        current_number = number
                        if known in mapped_input and mapped_input[known] > 0:
                            print(number)
                            while mapped_input[known] > 0:
                                for l in letters[number]:
                                    print(mapped_input)
                                    mapped_input[l] -= 1
                                result.append(number)
                        used.remove(number)
                    if is_ok(mapped_input):
                        result.sort()

                if is_ok(mapped_input):
                    result.sort()
                else:
                    print('3rd round')
                    # other numbers
                    for known, number in mapping_3.iteritems():
                        current_number = number
                        if known in mapped_input and mapped_input[known] > 0:
                            print(number)
                            while mapped_input[known] > 0:
                                for l in letters[number]:
                                    print(mapped_input)
                                    mapped_input[l] -= 1
                                result.append(number)
                        used.remove(number)
                    if is_ok(mapped_input):
                        result.sort()

                print_result = "".join(map(lambda a: str(a), result))
                print("Case #{0}: {1}".format(case_number, print_result))
                out.write("Case #{0}: {1}\n".format(case_number, print_result))
                