numbers = {
    0: "ZERO", 
    1: "ONE", 
    2: "TWO", 
    3: "THREE", 
    4: "FOUR", 
    5: "FIVE", 
    6: "SIX", 
    7: "SEVEN", 
    8: "EIGHT", 
    9: "NINE"
}

def solving(s):
    ch = {'I': 0, 'Z': 0, 'W': 0,'H': 0, 'U': 0, 'X': 0, 'G': 0, 'O': 0, 'F': 0, 'S': 0, 'N': 0}
    list = []
    for c in s:
        if c not in ch:
            ch[c] = 0
        ch[c] += 1
    # 'z' for 0
    fun(ch['Z'], 0,list,ch)
    fun(ch['W'], 2,list,ch)
    fun(ch['U'], 4,list,ch)
    fun(ch['X'], 6,list,ch)
    fun(ch['G'], 8,list,ch)
    fun(ch['H'], 3,list,ch)
    fun(ch['O'], 1,list,ch)
    fun(ch['F'], 5,list,ch)
    fun(ch['S'], 7,list,ch)
    fun(ch['I'], 9,list,ch)
    for s in ch:
        if s != '\n' and ch[s] != 0:
            print ch
            print 'error'
    so = sorted(list)
    return ''.join([str(c) for c in so])

def fun(n_d, d,list1,ch):
    if n_d == 0:
        return
    for sc in numbers[d]:
        ch[sc] = ch[sc] - n_d
        if ch[sc] < 0:
            print 'error', n_d, d
    for i in range(n_d):
        list1.append(d)

with open('input', 'r') as input:
	count = 0
	for line in input:
		if count == 0:
			count+=1
			continue
		print 'Case #%d: %s' % (count, solving(line))
		count+=1