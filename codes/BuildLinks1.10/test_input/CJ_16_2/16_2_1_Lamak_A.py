import random
fw = open("output.out", "w")

found = False
phoneNumber = ''
m = {'ZERO': '0', 'ONE': '1', 'TWO': '2', 'THREE': '3', 'FOUR': '4', 'FIVE': '5', 'SIX': '6', 'SEVEN': '7', 'EIGHT': '8', 'NINE': '9'}
words = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
def getCases():
    with open("A-small-attempt0.in") as f:
        lines = f.read().splitlines() 
        T = int(lines[0])
        for t in range(1, T + 1):
            s = lines[t]
            yield {'t': t, 's': s}

def getMyCases():
    yield {'t': 1, 's': ''}

def rem(a, num):
    rem = a
    for c in num:
        rem = rem.replace(c, '', 1)
    if len(a) - len(rem) == len(num):
        return {'pass': True, 'rem': rem}
    return {'pass': False}

def build(s, wordCount, ph):
    global found
    global phoneNumber
    if len(s) == 0:
        found = True
        phoneNumber = ph
        return
    for w in range(wordCount, 10):
        r = rem(s, words[w])
        if r['pass']:
            build(r['rem'], w, ph + m[words[w]])
        build(s, w + 1, ph)
        
for T in getCases():
    build(T['s'], 0, '')
    print ('Case #' + str(T['t']) + ': ' + phoneNumber)
    fw.write('Case #' + str(T['t']) + ': ' + phoneNumber + '\n')


fw.close()
