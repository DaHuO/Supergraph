def test_case(pan):
    moves = 0
    if happy(pan):
        return moves
    else:
        rightmost = pan.rfind("-")
        return flip(pan,rightmost, moves)
def flip(panc, pos, count):
    if len(panc) == 1:
        if panc == "-":
            panc = "+"
        else:
            panc = "-"
    else:
        for i in range(0, pos+1):
            if(panc[i] == "+"):
                panc = panc[0:i] + "-" + panc[i+1: len(panc)]
            elif(panc[i] == "-" and i == len(panc)-1):
                panc= panc[0:i] + "+"   
            else:
                panc= panc[0:i] + "+" + panc[i+1: len(panc)]
    count+=1
    if happy(panc):
        return count
    else:
        rightmost = panc.rfind("-")
        return flip(panc,rightmost, count)
def happy(s):
    if(s.find("-") == -1):
        return True
    else:
        return False
file_in = open(r"C:\Users\Isaac\Desktop\B-large.in")
file_out = open(r"C:\Users\Isaac\Desktop\panck.txt", mode="w")
numcases = file_in.readline()
cases = []

for x in range(0, int(numcases)):
    cases.append(file_in.readline())
    cases[x] = cases[x][0: len(cases[x])-1]
for x in range(0, len(cases)):
    #print("Case #" + str(x+1) + ": " + str(test_case(cases[x])))
    file_out.write("Case #" + str(x+1) + ": " + str(test_case(cases[x]))+ "\n")
file_in.close()
file_out.close()