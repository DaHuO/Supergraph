


dec = {"ZERO":0, "ONE":1,"TWO":2,"THREE":3, "FOUR":4, "FIVE":5,"SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}

numbs = ["ZERO", "TWO", "SIX", "EIGHT", "FOUR", "THREE", "SEVEN", "FIVE", "NINE", "ONE"]

def solve(numb):
    letters = {}
    numbers = []
    for letter in numb:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    for cap in numbs:
        more = True
        letters

        
        while(dicHasLetters(letters,cap)):
            for letter in cap:
                letters[letter] -= 1
            numbers.append(dec[cap])
    numbers.sort()
    s = ''
    for n in numbers:
        s += str(n)
#    count = 0
#    for letter in letters:
#        count += letters[letter]
#    if count > 0:
#        print numb, s, count
    return s

            
            


def dicHasLetters(dic, letters):
    has = True
    other = {}
    for letter in letters:
        if letter in other:
            other[letter] += 1
        else:
            other[letter] = 1

    
    for letter in other.keys():
        if letter in dic:
            if dic[letter] < other[letter]:
                return False
        else:
            return False
    return True

f = open('a.in', 'r')
g = open('a.out', 'w')

t = int(f.readline())

for i in range(1,t+1):

    #read input
    numb = f.readline().split('\n')[0]

    #solve
    ans = solve(numb)
    pr = "Case #"+str(i)+ ": " + str(ans)
    print pr
    g.write(pr + '\n')


f.close()
g.close()
