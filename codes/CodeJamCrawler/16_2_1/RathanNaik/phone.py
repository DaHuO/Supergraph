n=0;
n = eval(input())
number = []
no = ""
ans = []
dig =  []
digit = ""
for i in range(n):
    no = input().strip()
    number.append(no)
    no = list(no)
    while(len(no) != 0):
        while(no.__contains__("Z")):
            dig.append("0")
            no.remove("Z")
            no.remove("E")
            no.remove("R")
            no.remove("O")
        while(no.__contains__("W")):
            dig.append("2")
            no.remove("T")
            no.remove("W")
            no.remove("O")
        while(no.__contains__("U")):
            dig.append("4")
            no.remove("F")
            no.remove("O")
            no.remove("U")
            no.remove("R")
        while(no.__contains__("X")):
            dig.append("6")
            no.remove("S")
            no.remove("I")
            no.remove("X")
        while(no.__contains__("R")):
            dig.append("3")
            no.remove("T")
            no.remove("H")
            no.remove("R")
            no.remove("E")
            no.remove("E")
        while(no.__contains__("F")):
            dig.append("5")
            no.remove("F")
            no.remove("I")
            no.remove("V")
            no.remove("E")
        while(no.__contains__("G")):
            dig.append("8")
            no.remove("E")
            no.remove("I")
            no.remove("G")
            no.remove("H")
            no.remove("T")
        while(no.__contains__("I")):
            dig.append("9")
            no.remove("N")
            no.remove("I")
            no.remove("N")
            no.remove("E")
        while(no.__contains__("V")):
            dig.append("7")
            no.remove("S")
            no.remove("E")
            no.remove("V")
            no.remove("E")
            no.remove("N")
        while(no.__contains__("O")):
            dig.append("1")
            no.remove("O")
            no.remove("N")
            no.remove("E")
    dig.sort()
    for j in dig:
        digit += j
    ans.append(digit)
    digit = ""
    dig.clear()
j=1;
for i in ans:
    print("Case #",j,": ",i,sep="")
    j += 1
