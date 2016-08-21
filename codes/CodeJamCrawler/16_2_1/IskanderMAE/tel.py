import sys

if len(sys.argv) > 1: filename = sys.argv[1]
else: filename = "in.txt"
inFile = open(filename, "r")
outFile = open("out.txt", "w")


class PhoneAnalizer:
    def __init__(self, case_num, inp_str):
        self.inp_str = inp_str
        self.case_num = case_num
        self.res = ''

    def __repr__(self):
        #Case #1: 012
        return "Case #{0}: {1}".format(self.case_num, self.res)

    def count_letters(self):
        self.letters = {}
        for ch in self.inp_str:
            if ch in self.letters:
                self.letters[ch] += 1
            else:
                self.letters[ch] = 1

    def get_statistic(self):
        stat = ["E","F","G","H","I","N","O","R","S","T","U","V","W","X","Z"]
        self.statistic = {}
        def get_s(ch, st):
            i = 0
            for c in st:
                if c==ch: i += 1
            return i
        for ch in stat:
            self.statistic[ch] = get_s(ch, self.inp_str)

    def reduce_stat(self, numb, count):
        num_letter = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        for ch in num_letter[numb]:
            self.statistic[ch] -= count

    def resolve(self):
        self.count_letters()
        self.get_statistic()
        #print(self.statistic)

        arr = [[0,'Z'], [8,'G'], [6,'X'], [2,'W'], [3,'H'], [4,'R'], [5,'F'], [7,'V'], [1,'O'], [9,'I']]
        res = {}
        for x in arr:
            res[x[0]] = self.statistic[x[1]]
            self.reduce_stat(x[0], res[x[0]])
            #print(x[0], res[x[0]], self.statistic)

        for x in res:
             self.res += str(x)* res[x]

numCases = inFile.readline()

step = 1
st = inFile.readline()
while st.strip() !="":
    pa = PhoneAnalizer(step, st)
    pa.resolve()
    outFile.write("{0}\n".format(pa))
    step += 1
    st = inFile.readline()

outFile.close()
inFile.close()