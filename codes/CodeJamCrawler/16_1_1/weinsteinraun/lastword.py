from collections import deque

t = int(raw_input())

for i in xrange(t):
    word = raw_input().strip()
    resulting_word = deque()
    for c in word:
        try:
            first = resulting_word.popleft()
        except:
            resulting_word.append(c)
            continue

        resulting_word.appendleft(first)
        if c >= first:
            resulting_word.appendleft(c)
        else:
            resulting_word.append(c)
    result = ''.join(list(resulting_word))
            
    print "Case #{}: {}".format(i + 1, result)
