class Case:
    def __init__(self, id_case, file_in, file_out):
        self.res = ""
        self.number = None
        self.id_case = id_case
        self.soldiers = []
        self.res = []
        self.N = 0

        self.read(file_in)
        self.solve()
        self.write_output(file_out)
    def read(self, file):
        self.N = int(file.readline())
        for i in range(2*self.N-1):
            temp = file.readline().split()
            self.soldiers.append([])
            for i in temp:
                self.soldiers[-1].append(int(i))


    def write_output(self, file):
        file.write("Case #"+str(self.id_case)+": "+" ".join(self.res)+"\n")

    def solve(self):
        print("############ CASE : "+str(self.id_case))
        for h in range(1, 2501):
            if (self.compte_taille(h) % 2) != 0 :
                self.res.append(str(h))

    def compte_taille(self,h):
        res = 0
        for l in self.soldiers:
            for s in l:
                if h == s:
                    res += 1
                    break
        return res



file_in = open("B-large.in", 'r')
file_out = open("data.out", 'w')
for i in range(int(file_in.readline())):
    Case(i+1,file_in,file_out)