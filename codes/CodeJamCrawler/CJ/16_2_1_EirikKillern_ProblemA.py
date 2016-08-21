def letterCheck(string):
    dic = {}
    numbers = [0]*10
    for l in string:
        dic.setdefault(l,0)
        dic[l] += 1

    if "Z" in dic:
        if dic["Z"] > 0:
            dic["E"] -= dic["Z"]
            dic["R"] -= dic["Z"]
            dic["O"] -= dic["Z"]
            numbers[0] += dic["Z"]
            dic["Z"] = 0
    if "U" in dic:
        if dic["U"] > 0:
            dic["O"] -= dic["U"]
            dic["F"] -= dic["U"]
            dic["R"] -= dic["U"]
            numbers[4] += dic["U"]
            dic["U"] = 0
    if "X" in dic:
        if dic["X"] > 0:
            dic["I"] -= dic["X"]
            dic["S"] -= dic["X"]
            numbers[6] += dic["X"]
            dic["X"] = 0
    if "G" in dic:
        if dic["G"] > 0:
            dic["E"] -= dic["G"]
            dic["I"] -= dic["G"]
            dic["T"] -= dic["G"]
            dic["H"] -= dic["G"]
            numbers[8] += dic["G"]
            dic["G"] = 0
    if "W" in dic:
        if dic["W"] > 0:
            dic["T"] -= dic["W"]
            dic["O"] -= dic["W"]
            numbers[2] += dic["W"]
            dic["W"] = 0
    if "S" in dic:
        if dic["S"] > 0:
            dic["E"] -= dic["S"]*2
            dic["V"] -= dic["S"]
            dic["N"] -= dic["S"]
            numbers[7] += dic["S"]
            dic["S"] = 0
    if "V" in dic:
        if dic["V"] > 0:
            dic["E"] -= dic["V"]
            dic["I"] -= dic["V"]
            dic["F"] -= dic["V"]
            numbers[5] += dic["V"]
            dic["V"] = 0
    if "I" in dic:
        if dic["I"] > 0:
            dic["E"] -= dic["I"]
            dic["N"] -= dic["I"]*2
            numbers[9] += dic["I"]
            dic["I"] = 0
    if "R" in dic:
        if dic["R"] > 0:
            dic["E"] -= dic["R"]*2
            dic["H"] -= dic["R"]
            dic["T"] -= dic["R"]
            numbers[3] += dic["R"]
            dic["R"] = 0
    if "O" in dic:
        numbers[1] += dic["O"]
    output_str = ""
    for i in range(0,10):
        output_str += str(i)*numbers[i]
    return output_str





def main():
    fil = open('input.txt','r')
    output = open('output.txt','w')
    cases = fil.readline()
    print(cases)
    for i in range(int(cases)):
        string = fil.readline()
        output.write("Case #"+str(i+1)+": " +letterCheck(string)+"\n")
    output.close()
    fil.close()
main()