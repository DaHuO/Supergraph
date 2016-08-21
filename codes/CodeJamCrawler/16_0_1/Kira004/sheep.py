from sys import argv
class Solution(object):
    def sheep(self, x):
        if x == 0:
            return "INSOMNIA"
        dmap = set()
        i = 1
        while (len(dmap) < 10):
            self.showupDigit(x*i, dmap)
            i += 1
        return str(x*(i-1))
        
    def showupDigit(self, v, dmap):
        while v > 0:
            t = v % 10
            dmap.add(t)
            v = int(v/10)

if __name__ == "__main__":
    try:
        filename = argv[1]
        try:
            f = open(filename)
            nf = open(filename[:-2]+"out", "w")
    
            sol = Solution()
            n = int(f.readline())
            for i in range(n):
                x = int(f.readline())
                t = sol.sheep(x)
                nf.write("Case #%d: %s\n" % (i+1, t))
        except IOError:
            print ("No such file: %s" % filename)
    except IndexError:
        print ("Too few parameters!")
        print ("Usage: python sheep.py inputfile")
