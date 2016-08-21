cases = int(input())
digits = {0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE"}

def test(s):
    #print("testing " + str(s))
    if len(s) == 0:
        return []
    chars = set(s)
    for digit in digits.keys():
        rep = digits[digit]
        contains_digit = True
        for rep_char in set(rep):
            if rep.count(rep_char) > s.count(rep_char):
                contains_digit = False

        if not contains_digit:
            continue

        for rep_char in rep:
            s = s.replace(rep_char, "", 1)
        #print("found "+str(digit))
        rest = test(s)
        if rest == -1:
            # undo
            s += rep
            #print("undid "+str(digit))
        else:
            return [digit] + rest
    return -1

for t in range(cases):
    s = input()
    number = test(s)
    number = [str(n) for n in number]
    print("Case #"+str(t+1)+": "+"".join(number))