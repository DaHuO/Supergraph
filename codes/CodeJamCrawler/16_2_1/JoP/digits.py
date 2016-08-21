from collections import Counter
import sys

def subtract_word(freq, word, n):
    a, b = freq, Counter(word)
    for i in range(0,n):
        a = {key: a[key] - b.get(key, 0) for key in a.keys()}
    return a

def getnumber(word):
    freq = Counter(word)
    res = [0] * 10

    res[0] = freq.get("Z", 0)
    freq = subtract_word(freq, "ZERO", res[0])
    res[2] = freq.get("W", 0)
    freq = subtract_word(freq, "TWO", res[2])
    res[4] = freq.get("U", 0)
    freq = subtract_word(freq, "FOUR", res[4])
    res[6] = freq.get("X", 0)
    freq = subtract_word(freq, "SIX", res[6])
    res[8] = freq.get("G", 0)
    freq = subtract_word(freq, "EIGHT", res[8])
    res[1] = freq.get("O", 0)
    freq = subtract_word(freq, "ONE", res[1])
    res[3] = freq.get("T", 0)
    freq = subtract_word(freq, "THREE", res[3])
    res[5] = freq.get("F", 0)
    freq = subtract_word(freq, "FIVE", res[5])
    res[7] = freq.get("S", 0)
    freq = subtract_word(freq, "SEVEN", res[7])
    res[9] = freq.get("E", 0)
    freq = subtract_word(freq, "NINE", res[9])

    for i in freq.keys():
        if freq[i] != 0 and i != "\n":
            print("ERRROR",freq,word)
    
    no = ""
    for i in range(0,10):
        no += ''.join([str(i)]*res[i])
    return no

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(0,N):
        w = sys.stdin.readline()
        print("Case #{}:".format(i+1), getnumber(w))
    
    
    
    
    
