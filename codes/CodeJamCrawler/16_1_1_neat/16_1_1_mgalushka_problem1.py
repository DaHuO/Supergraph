from sets import Set

def digits(number):
    r = []
    for digit in str(number):
        r.append(digit)
    return Set(r)

if __name__ == "__main__":
    data = []
    T = 0
    with open('/Users/mgalushka/google_code_jam/round1a/output1.out', 'w') as out:
        with open('/Users/mgalushka/google_code_jam/round1a/input1', 'r') as inp:
            T = int(inp.readline().strip())
            for case_number in range(1, T+1):
                S = inp.readline().strip()
                now = []
                for letter in S:
                    if len(now) == 0:
                        now.append(letter)
                    else:
                        first = now[0]
                        if letter >= first:
                            now.insert(0, letter)
                        else:
                            now.append(letter)
                result = "".join(now)
                print("Case #{0}: {1}".format(case_number, result))
                out.write("Case #{0}: {1}\n".format(case_number, result))
                