import sys

DIGIT = {
    '0': 'ZERO',
    '1': 'ONE',
    '2': 'TWO',
    '3': 'THREE',
    '4': 'FOUR',
    '5': 'FIVE',
    '6': 'SIX',
    '7': 'SEVEN',
    '8': 'EIGHT',
    '9': 'NINE',
}

class WordCounter():
    def __init__(self, word):
        self.count = {}
        for w in word:
            self.set(w)
    def set(self, w):
        self.count.setdefault(w, 0)
        self.count[w] += 1
    def total(self):
        count = 0
        for k, c in self.count.iteritems():
            count += c
        return count
    def __eq__(self, wc):
        for k, c in self.count.iteritems():
            if not (k in wc.count and wc.count[k] == c):
                return False
        return True
                
def num2word_count(num):
    return sum([len(DIGIT[n]) for n in num])

def num2word(num):
    word = ''
    for n in num:
        word += DIGIT[n]
    return word

def z_count(word):
    count = 0
    for w in word:
        if w == 'Z':
            count += 1
    return count

def try_num(n, word, zc):
    #print 'try_num', n, word, zc
    for z_n in range(zc+1):
        num_s = str(n)
        for i in range(z_n):
            num_s = '0' + num_s
        #print num_s, num2word_count(num_s)
        num_word = num2word(num_s)
        if len(num_word) == len(word):
            #print '%s\n%s' % (WordCounter(word).count, WordCounter(num_word).count)
            if WordCounter(word) == WordCounter(num_word):
                return num_s
    return None

def number(word):
    zc = z_count(word)
    for i in range(10000000):
        res = try_num(i, word, zc)
        if res:
            return res

def main():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        count = int(f.readline())
        for i in range(count):
            line = f.readline()
            num = number(line.strip())
            print 'Case #%d: %s' % (i+1, num)
            
    

if __name__ == '__main__':
    main()
