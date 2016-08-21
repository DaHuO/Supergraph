import sys

sys.stdin = open("A-large.in", "r")
sys.stdout = open("out.txt", "w")

test_case = int(input())

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
digits_counter = [None] * 10
for i in range(10):
    digits_counter[i] = [0]*26
    for c in digits[i]:
        digits_counter[i][ord(c) - 65] += 1

mapper = [('Z', 0), ('W', 2), ('U', 4), ('X', 6), ('G', 8), ('O', 1), ('H', 3),
        ('F', 5), ('S', 7), ('E', 9)]

def sol(s):
    counter = [0] * 26
    numbers = [0] * 10
    for c in s:
        if c.isalpha():
            counter[ord(c) - 65] += 1

    for c, n in mapper:
        count = counter[ord(c) - 65]
        if count != 0:
            numbers[n] = count
            for i in range(26):
                counter[i] -= digits_counter[n][i] * count
    ret = ""
    for i in range(10):
        ret += (str(i) * numbers[i])
    return ret

for i in range(test_case):
    input_s = input()
    phone_number = sol(input_s)
    print("Case #%d: %s"%(i+1, phone_number))

sys.stdout.close()
