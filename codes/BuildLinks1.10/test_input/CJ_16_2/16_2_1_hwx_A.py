
# coding: utf-8

# In[33]:

mapping = []
words = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
while words:
    unique = []
    for i in range(len(words)):
        unique.append(set(words[i]) - set(''.join(words[:i] + words[i+1:])))

    mapping.extend([[list(unique[i])[0], words[i]] for i in range(len(words)) if unique[i] != set()])
    words = [words[i] for i in range(len(words)) if unique[i] == set()]


# In[60]:

mapping[-1] = ['I', 'NINE']


# In[55]:

pdb


# In[64]:

#fin = r'A-samp.in'
fin = r'A-small-attempt1.in'
#fin = r'A-large.in'
from collections import Counter
with open(fin, 'r') as f:
    inputs = f.readlines()
results = []

words = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
num_lut = {words[i]: i for i in range(10)}
word_lut = {i:words[i] for i in range(10)}

for line in inputs[1:]:
    res = []
    cnt = Counter(line.strip())

    for ch, w in mapping:
        rep = cnt[ch]
        if rep:
            res.extend([num_lut[w]] * rep)
            for c in w:
                cnt[c] -= rep
    for k, v in cnt.items():
        assert(v==0)
    results.append(''.join(map(str, sorted(res))))


# In[65]:

fout = fin.replace('.in','.out')

with open(fout, 'w') as f:
    for i, res in enumerate(results):
        f.write("Case #%d: %s\n" % (i+1, res))


# In[ ]:



