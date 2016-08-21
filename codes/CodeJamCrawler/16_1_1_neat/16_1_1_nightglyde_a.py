import sys

cin = sys.stdin.readlines()

T = int(cin[0].strip())
for case in range(1, T+1):
    letters = cin[case].strip()
    word = letters[0]
    for i in range(1, len(letters)):
        letter = letters[i]
        if letter >= word[0]:
            word = letter + word
        else:
            word += letter
    print("Case #{}: {}".format(case, word))

