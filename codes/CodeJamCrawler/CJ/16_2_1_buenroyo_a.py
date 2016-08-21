digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
          "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

dic = {}
df = {}

for i in xrange(10):
    digit = digits[i]
    df[i] = {}
    for letter in digit:
        if letter in dic:
            if i not in dic[letter]: dic[letter].append(i)
        else: dic[letter] = [i]
        if letter in df[i]: df[i][letter] += 1
        else: df[i][letter] = 1

def consumeNumber(stack, numbers):
    #print stack, numbers
    if len(stack) > 0:
        letter = stack[0]
        candidates = dic[letter]
        for c in candidates:
            digit = digits[c]
            allIn = True
            for l in digit:
                if l not in df[c] or l not in freqs or freqs[l] < df[c][l]:
                    allIn = False
            if allIn:
                for l in digit:
                    del stack[stack.index(l)]
                    freqs[l] -= 1
                numbers.append(str(c))
                possible = consumeNumber(stack, numbers)
                if possible: return True
                del numbers[-1]
                for l in digit: stack.append(l); freqs[l] += 1
        return False
    return True

T=int(raw_input())
for t in xrange(1, T+1):
    S = raw_input()

    stack = list(S)
    freqs = {}

    for s in S:
        if s in freqs: freqs[s] += 1
        else: freqs[s] = 1
    
    numbers = []
    consumeNumber(stack, numbers)

    numbers.sort()
    res = "".join(numbers)
    print "Case #%d: %s"% (t, res)
