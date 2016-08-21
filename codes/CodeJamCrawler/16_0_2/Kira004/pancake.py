from sys import argv
class Solution(object):
    def pancake(self, p):
        count = 0
        for i in range(1, len(p)): 
            if p[i] != p[i-1]:
                count += 1
        if p[-1] == '-':
            count += 1
        return count

if __name__ == "__main__":
    try:
        filename = argv[1]
        try:
            f = open(filename)
            nf = open(filename[:-2]+"out", "w")
    
            sol = Solution()
            n = int(f.readline())
            for i in range(n):
                p = f.readline().strip()
                t = sol.pancake(p)
                nf.write("Case #%d: %d\n" % (i+1, t))
        except IOError:
            print ("No such file: %s" % filename)
    except IndexError:
        print ("Too few parameters!")
        print ("Usage: python pancake.py inputfile")
