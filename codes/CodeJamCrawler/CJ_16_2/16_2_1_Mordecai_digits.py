numdic = {'Z': 0, 'W': 2, 'U': 4, 'G': 8, 'X': 6, 'F': 5, 'I': 9, 'V': 7,
          'R': 3, 'O': 1}
strdic = {'Z': 'ZERO', 'W': 'TWO', 'U': 'FOUR', 'G': 'EIGHT', 'X': 'SIX',
         'F': 'FIVE', 'I': 'NINE', 'V': 'SEVEN', 'R': 'THREE', 'O': 'ONE'}
keys = ['Z', 'W', 'U', 'G', 'X', 'F', 'F', 'I', 'V', 'R', 'O']

def decifer(S):
    S = list(S)
    el = []
    for k in keys:
        if len(S) == 0: break
        while k in S:
            el.append(numdic[k])
            for letter in strdic[k]:
                S.pop(S.index(letter))
        if len(S) == 0: break
    return ''.join(map(str, sorted(el)))

def main():
    cases = int(raw_input())
    for case in range(1, cases+1):
        word = raw_input().strip()
        print "Case #%i:" %case, decifer(word)

if __name__ == '__main__':
    main()
