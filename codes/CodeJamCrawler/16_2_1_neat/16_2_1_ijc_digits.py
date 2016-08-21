from collections import Counter

digitMap = list(map(Counter, ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']))

def superset(a, b):
    for element in b.keys():
        if a[element] < b[element]:
            return False
    return True

def findDigits(s):
    s = Counter(s)
    digits = []
    for i in [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]:
        while superset(s, digitMap[i]):
            digits.append(i)
            s -= digitMap[i]
    return sorted(digits)

def main():
    T = int(input())
    for i in range(T):
        s = input()
        print("Case #{}: {}".format(i+1, ''.join(map(str, findDigits(s)))))

if __name__ == '__main__':
    main()
