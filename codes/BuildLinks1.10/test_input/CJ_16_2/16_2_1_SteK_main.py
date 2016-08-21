class Case:
    def __init__(self, id_case, file_in, file_out):
        self.res = []
        self.id_case = id_case
        self.S = []
        self.word = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.detect_order = [[(0,'Z'), (2,'W'), (4,'U'), (6,'X'), (8,'G')],
                             [(1,'O'),(3,'H'), (5,'F'), (7,'S')],
                             [(9,'N')]]
        self.read(file_in)
        self.solve()
        self.write_output(file_out)

    def read(self, file):
        self.S = list(file.readline())

    def write_output(self, file):
        file.write("Case #"+str(self.id_case)+": "+"".join(self.res)+"\n")

    def solve(self):
        print("############ CASE : "+str(self.id_case))
        print(self.S)
        for step in self.detect_order:
            for digit in step:
                while digit[1] in self.S:
                    print("Find : ",digit)
                    for c in self.word[digit[0]]:
                        print("Removing : ",c)
                        self.S.remove(c)
                    self.res.append(str(digit[0]))
        self.res.sort()


file_in = open("A-large.in", 'r')
file_out = open("data.out", 'w')
for i in range(int(file_in.readline())):
    Case(i+1,file_in,file_out)