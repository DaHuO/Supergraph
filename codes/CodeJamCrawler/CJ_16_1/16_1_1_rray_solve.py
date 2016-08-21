def last_word(s):
    word = s[0]
    for c in s[1:]:
        if c >= word[0]:
            word = c + word
        else:
            word = word + c
    return word

def main():
    t = int(raw_input())
    for i in xrange(t):
        print "Case #{}: {}".format(i+1, last_word(raw_input().strip()))

if __name__ == '__main__':
    main()
