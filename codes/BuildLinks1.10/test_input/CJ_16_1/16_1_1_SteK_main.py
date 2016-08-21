class Case:
    def __init__(self, id_case, file_in, file_out):
        self.res = ""
        self.number = None
        self.id_case = id_case
        self.read(file_in)
        self.solve()
        self.write_output(file_out)
        self.S = ""
        self.res = ""

    def read(self, file):
        self.S = file.readline()[:-1]

    def write_output(self, file):
        file.write("Case #"+str(self.id_case)+": "+str(self.res)+"\n")

    def solve(self):
        print("############ CASE : "+str(self.id_case))
        for c in self.S:
            if self.res == "":
                self.res += c
            elif self.res[0] > c:
                self.res += c
            else:
                self.res = c + self.res




file_in = open("A-large.in", 'r')
file_out = open("data.out", 'w')
for i in range(int(file_in.readline())):
    Case(i+1,file_in,file_out)