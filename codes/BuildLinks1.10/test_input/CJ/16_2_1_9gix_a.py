import collections

class Phone(object):
    def __init__(self, s):
        self.char_freq = collections.Counter(s.lower())
        self.no_list = []

    def remove(self, char, residual_chars, digit_repr):
        for i in range(self.char_freq[char]):
            self.no_list.append(digit_repr)
            for c in residual_chars:
                self.char_freq[c] -= 1

    def calculate(self):
        self.remove('w', 'to', '2')
        self.remove('z', 'ero', '0')
        self.remove('x', 'si', '6')
        self.remove('g', 'eiht', '8')
        self.remove('s', 'even', '7')
        self.remove('v', 'fie', '5')    
        self.remove('f','our', '4')
        self.remove('h', 'tree', '3')
        self.remove('i', 'nne', '9')
        self.remove('o', 'ne', '1')
        self.no_list.sort()
        return ''.join(self.no_list)

def main():
    t = int(input())
    for i in range(1, t + 1):
        s = input()
        p = Phone(s)
        last_word = p.calculate()
        print("Case #{}: {}".format(i, last_word))

if __name__ == '__main__':
    main()