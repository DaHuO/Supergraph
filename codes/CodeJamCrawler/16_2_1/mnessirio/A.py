task = "A-large"
infile = open('in/%s.in' % task, 'r')
outfile = open('out/%s.out' % task, 'w')
T = int(infile.readline())
print("Hi Sweety =)")
numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
           "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

# count_letters = {}
# for i in range(10):
#     for l in numbers[i]:
#         try:
#             count_letters[l].append(i)
#         except:
#             count_letters[l] = [i, ]
# for l in count_letters.keys():
#     print(l, count_letters[l])

pick_order = [
    {'Z': 0, 'W': 2, 'U': 4, 'G': 8, 'X': 6},
    {'H': 3, 'F': 5, 'S': 7},
    {'I': 9}
]


def solve():
    phone_number_digits = [0 for i in range(10)]
    S = list(infile.readline().strip())
    # print(S)
    for group in pick_order:
        for letter in group.keys():
            # take out all appearances of the letter
            # and number related to this letter
            while letter in S:
                phone_number_digits[group[letter]] += 1
                for x in numbers[group[letter]]:
                    S.remove(x)
    phone_number_digits[1] = len(S) // 3
    result = ""
    for i in range(len(phone_number_digits)):
        #print(str(i), phone_number_digits[i], str(i) * phone_number_digits[i])
        result += str(i) * phone_number_digits[i]
#     print(result)
    return result

for case in range(1, T + 1):
    #     print(case)
    outfile.write("Case #%d: %s\n" % (case, solve()))

infile.close()
outfile.close()
