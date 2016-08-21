FILE = "/Users/jiajunliang/Downloads/A-large (1).in"
digits = ["ZERO", #Z
          "ONE",
          "TWO",  #W
          "THREE",
          "FOUR", #U
          "FIVE",
          "SIX",#X
          "SEVEN",
          "EIGHT", #G
          "NINE"]

digits = map(lambda d : "".join(sorted(list(d))), digits)
#print digits

table = None

def userless():
    found = False
    ans = None
    def solve(s, cur):
        #print "solving: {}, cur: {}".format(s,cur)
        global found, ans
        if not found:
            if len(s) == 0:
                found = True
                ans = cur
                return
            for ind,d in enumerate(digits):
                if len(d) <= len(s):
                    if d == "".join(sorted(list(s[0:len(d)]))):
                        if len(cur) == 0 or int(cur[-1]) <= ind:
                            solve(s[len(d):], cur + str(ind))


def judge(word):
    for c in word:
        if table[c] <= 0:
            return False
    return True

def update_table(word):
    for c in word:
        table[c] -= 1

def recover_table(word):
    for c in word:
        table[c] += 1

word2num = {"ONE" : 1,
            "THREE" : 3,
            "FIVE" : 5,
            "SEVEN" : 7,
            "NINE" : 9}

word_list = [
          "ONE",
          "THREE",
          "FIVE",
          "SEVEN",
          "NINE"]
def solve(s):
    global table
    global word_list
    global word2num
    def dfs(total, ans):
        #print total, ans
        if total == 0:
            return True
        else:
            for word in word_list:
                if judge(word):
                    update_table(word)
                    total -= len(word)
                    ans.append(word2num[word])
                    ret = dfs(total, ans)
                    if not ret:
                        recover_table(word)
                        total += len(word)
                        del ans[-1]
                    else:
                        return True
        return False
    ans = []
    total = len(s)
    for c in s:
        table[c] += 1
    while(table['Z'] > 0):
        for c in "ZERO":
            table[c] -= 1
            total -= 1
        ans.append(0)
    while(table['W'] > 0):
        for c in "TWO":
            table[c] -= 1
            total -= 1
        ans.append(2)
    while(table['U'] > 0):
        for c in "FOUR":
            table[c] -= 1
            total -= 1
        ans.append(4)

    while(table['X'] > 0):
        for c in "SIX":
            table[c] -= 1
            total -= 1
        ans.append(6)

    while(table['G'] > 0):
        for c in "EIGHT":
            table[c] -= 1
            total -= 1
        ans.append(8)

    if total > 0:
        dfs(total, ans)

    return ans


with open(FILE) as f:
    lines = f.readlines()
    T = int(lines[0])
    t = 1
    while t <= T:
        s = lines[t].strip()
        table = {chr(c):0 for c in range(ord('A'), ord('Z') + 1)}
        #print s
        ans = solve(s)
        print "Case #{}: {}".format(t,"".join(map(str,sorted(ans))))

        #solve(s, "")
        #print ans
        t += 1

#print "test"
#s = "FREIVZEO"
#table = {chr(c):0 for c in range(ord('A'), ord('Z') + 1)}
#print solve(s)
