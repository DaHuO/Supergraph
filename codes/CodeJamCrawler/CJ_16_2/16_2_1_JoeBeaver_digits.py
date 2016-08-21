filename = "A-large.in"

letters = ['Z', 'O', 'W', 'H', 'U', 'F', 'X', 'V', 'G', 'I']

def analyze(caseNumber, numberString):
    counts = [0] * 10
    letterCounts = {let: numberString.count(let) for let in letters}

    counts[0] = letterCounts['Z']
    letterCounts['O'] -= letterCounts['Z']

    counts[2] = letterCounts['W']
    letterCounts['O'] -= letterCounts['W']
    
    counts[4] = letterCounts['U']
    letterCounts['O'] -= letterCounts['U']
    letterCounts['F'] -= letterCounts['U']

    counts[5] = letterCounts['F']
    letterCounts['V'] -= letterCounts['F']
    letterCounts['I'] -= letterCounts['F']

    counts[6] = letterCounts['X']
    letterCounts['I'] -= letterCounts['X']

    counts[7] = letterCounts['V']

    counts[8] = letterCounts['G']
    letterCounts['H'] -= letterCounts['G']
    letterCounts['I'] -= letterCounts['G']

    counts[3] = letterCounts['H']

    counts[1] = letterCounts['O']

    counts[9] = letterCounts['I']

    phone = ""
    for i in range(10):
        phone += str(i) * counts[i]
    
    return "Case #%s: %s" % (caseNumber, phone)


with open(filename, 'r') as f, open(filename[:-2] + "out", 'w') as out:
    t = int(f.readline())
    for i in range(1, t + 1):
        out.write(analyze(i, f.readline()) + '\n')
