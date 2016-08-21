__author__ = 'gambler'
class Solution:
    def solve(self):
        N = ar[0]
        J = ar[1]
        divline = " 3 4 5 6 7 8 9 10 11\n"
        di = dict()
        if N==16:
            even = [2,4,6,8,10,12,14]
            odd = [1,3,5,7,9,11,13]
            for e in even:
                for o in odd:
                    ans = list('1' + 14*'0' + '1')
                    ans[e] = '1'
                    ans[o] = '1'
                    val = "".join(ans)
                    di[val] = 1
                    fout.write(val + divline)
            fout.write("1000000000000001"+divline)
        else:
            even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]#,32,34,36,38,40,42,44,46,48]
            odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]#,31,33,35,37,39,41,43,45,47,49]
            for e1 in even:
                for o1 in odd:
                    for e2 in even:
                        for o2 in odd:
                            ans = list('1' + 30*'0' + '1')
                            ans[e1] = '1'
                            ans[o1] = '1'
                            ans[e2] = '1'
                            ans[o2] = '1'
                            val = "".join(ans)
                            di[val] = 1
                            fout.write(val + divline)
                            if len(di)==499:
                                break
                        if len(di)==499:
                            break
                    if len(di)==499:
                        break
                if len(di)==499:
                    break
            fout.write("10000000000000000000000000000001"+divline)
        #print len(di)



#fin = open("/Users/gambler/Documents/pycharm/input.txt", "r")
fin = open("/Users/gambler/Documents/pycharm/C-small-attempt0.in", "r")
fout = open("/Users/gambler/Documents/pycharm/output.txt", "w")
cases = int(fin.readline().strip())
s = Solution()
for case in range(cases):
    ar = map(int, fin.readline().strip().split())
    fout.write("Case #"+str(case+1)+":\n")
    s.solve()

fin.close()
fout.close()
