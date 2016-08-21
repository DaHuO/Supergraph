# def solve(N):
#     return str(N)

# if __name__ == "__main__":
#     T = int(input())
#     for t in range(T):
#         N = int(input())
#         sol = solve(N)
#         out = "Case #%s: %s" % ((t+1), sol)
#         print(out)


# digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
# digits = ["ZERO", "TWO", "FOUR", "SIX", "EIGHT"]
# digits = ["ONE", "THREE", "FIVE", "SEVEN"]
# count = {}

# for d in digits:
#   # print(d)
#   for c in d:
#       # print(c)
#       if c not in count:
#           count[c] = 0
#       count[c] += 1

# print(count)



def construct_digits_count():
    digits_count = {}
    digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    for i in range(10):
        digits_count[i] = count_letters(digits[i])
    # print(digits_count)
    return digits_count

def count_letters(S):
    count = {}
    for c in S:
        if c not in count:
            count[c] = 0
        count[c] += 1
    return count

def solve(S):
    digits_count = construct_digits_count()
    count = count_letters(S)
    digits = {}

    if 'Z' in count:
        digits[0] = count['Z']
        count['Z'] -= digits[0]
        count['E'] -= digits[0]
        count['R'] -= digits[0]
        count['O'] -= digits[0]
    if 'W' in count:
        digits[2] = count['W']
        count['T'] -= digits[2]
        count['W'] -= digits[2]
        count['O'] -= digits[2]
    if 'U' in count:
        digits[4] = count['U']
        count['F'] -= digits[4]
        count['O'] -= digits[4]
        count['U'] -= digits[4]
        count['R'] -= digits[4]
    if 'X' in count:
        digits[6] = count['X']
        count['S'] -= digits[6]
        count['I'] -= digits[6]
        count['X'] -= digits[6]
    if 'G' in count:
        digits[8] = count['G']
        count['E'] -= digits[8]
        count['I'] -= digits[8]
        count['G'] -= digits[8]
        count['H'] -= digits[8]
        count['T'] -= digits[8]

    if 'O' in count and count['O'] > 0:
        digits[1] = count['O']
        count['O'] -= digits[1]
        count['N'] -= digits[1]
        count['E'] -= digits[1]
    if 'T' in count and count['T'] > 0:
        digits[3] = count['T']
        count['T'] -= digits[3]
        count['H'] -= digits[3]
        count['R'] -= digits[3]
        count['E'] -= digits[3]
        count['E'] -= digits[3]
    if 'F' in count and count['F'] > 0:
        digits[5] = count['F']
        count['F'] -= digits[5]
        count['I'] -= digits[5]
        count['V'] -= digits[5]
        count['E'] -= digits[5]
    if 'S' in count and count['S'] > 0:
        digits[7] = count['S']
        count['S'] -= digits[7]
        count['E'] -= digits[7]
        count['V'] -= digits[7]
        count['E'] -= digits[7]
        count['N'] -= digits[7]

    if 'I' in count and count['I'] > 0:
        digits[9] = count['I']
        count['N'] -= digits[9]
        count['I'] -= digits[9]
        count['N'] -= digits[9]
        count['E'] -= digits[9]
    
    # print(digits)

    sol = ""
    for i in range(10):
        if i in digits:
            for j in range(digits[i]):
                sol += str(i)
    # print(sol)
    return sol

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        S = input()
        sol = solve(S)
        out = "Case #%s: %s" % ((t+1), sol)
        print(out)


# solve("OZONETOWER")
# solve("WEIGHFOXTOURIST")
# solve("OURNEONFOE")
# solve("ETHER")
