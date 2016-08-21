from sys import argv
class Solution(object):
    def digits(self, x):
        d = {}
        for c in x:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        dig = {0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE"}
        even = {'G':8,'X':6,'Z':0,'W':2,'U':4}
        odd = {'O':1,'R':3,'S':7,'H':3,'T':3,'F':5}

        res = []
        for c in x:
            if d[c] == 0: continue
            if c in even:
                res.append(even[c])
                for i in dig[even[c]]:
                    d[i] -= 1
        for c in x:
            if d[c] == 0: continue
            if c in odd:
                res.append(odd[c])
                for i in dig[odd[c]]:
                    d[i] -= 1

        if 'I' in d: 
            for i in range(d['I']):
                res.append(9)
        res = sorted(res)
        return "".join(map(str, res))


if __name__ == "__main__":
    try:
        filename = argv[1]
        try:
            f = open(filename)
            nf = open(filename[:-2]+"out", "w")
    
            sol = Solution()
            t = int(f.readline())
            for i in range(t):
                x = f.readline().strip()
                y = sol.digits(x)
                nf.write("Case #%d: %s\n" % (i+1, y))
        except IOError:
            print ("No such file: %s" % filename)
    except IndexError:
        print ("Too few parameters!")
        print ("Usage: python digits.py inputfile")
