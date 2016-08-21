import numpy as np

def f(s):
    if s == []: return []
    c = s[np.argmax(s)]

    maxs = np.where(np.array(s) == c)[0]
    return max([([c] + f(s[:i]) + s[i+1:]) for i in maxs])
    
t=input()
import fileinput
words =  map(lambda s: list(s[:-1]),fileinput.input())[:t]

template = "Case #%d: %s"
for (i, r) in enumerate(map(f, words)):
    print(template % (i+1,''.join(r)))

