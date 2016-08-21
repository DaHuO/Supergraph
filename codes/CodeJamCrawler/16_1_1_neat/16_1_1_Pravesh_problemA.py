file = open("input.in", "r").readlines()
T = int(file.pop(0))
i = 1

result = set("0123456789")

def get_last_word(S, word=''):
    for s in S:
        if word == '':
            word = s
        else:
            if ord(s) >= ord(word[0]):
                word = s+word
            else:
                word = word + s
    return word

while i <= T:
    S = file.pop(0).strip()
    print("Case #%d:" % i, get_last_word(S))
    i += 1
