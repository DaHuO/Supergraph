import re

i = int(input())
for case in range(i):
    string = str(input())
    ret = ""
    while string:
        while("Z" in string):
            ret += "0"
            string = re.sub("Z(.*)","\\1",string)
            string = re.sub("E(.*)","\\1",string)
            string = re.sub("R(.*)","\\1",string)
            string = re.sub("O(.*)","\\1",string)
        while("G" in string):
            ret += "8"
            string = re.sub("E(.*)","\\1",string)
            string = re.sub("I(.*)","\\1",string)
            string = re.sub("G(.*)","\\1",string)
            string = re.sub("H(.*)","\\1",string)
            string = re.sub("T(.*)","\\1",string)
        
        while("W" in string):
            ret += "2"
            string = re.sub("T(.*)","\\1",string)
            string = re.sub("W(.*)","\\1",string)
            string = re.sub("O(.*)","\\1",string)
        
        while("H" in string):
            ret += "3"
            string = re.sub("T(.*)","\\1",string)
            string = re.sub("H(.*)","\\1",string)
            string = re.sub("R(.*)","\\1",string)
            string = re.sub("E(.*)","\\1",string)
            string = re.sub("E(.*)","\\1",string)
        
        while("U" in string):
            ret += "4"
            string = re.sub("F(.*)","\\1",string)
            string = re.sub("O(.*)","\\1",string)
            string = re.sub("U(.*)","\\1",string)
            string = re.sub("R(.*)","\\1",string)
            
        while("F" in string):
            ret += "5"
            string = re.sub("F(.*)","\\1",string)
            string = re.sub("I(.*)","\\1",string)
            string = re.sub("V(.*)","\\1",string)
            string = re.sub("E(.*)","\\1",string)
            
        while("O" in string):
            ret += "1"
            string = re.sub("O(.*)","\\1",string)
            string = re.sub("N(.*)","\\1",string)
            string = re.sub("E(.*)","\\1",string)
        
        while("X" in string):
            ret += "6"
            string = re.sub("S(.*)","\\1",string)
            string = re.sub("I(.*)","\\1",string)
            string = re.sub("X(.*)","\\1",string)
            
        while("S" in string):
            ret += "7"
            string = re.sub("S(.*)","\\1",string)
            string = re.sub("E(.*)","\\1",string)
            string = re.sub("V(.*)","\\1",string)
            string = re.sub("E(.*)","\\1",string)
            string = re.sub("N(.*)","\\1",string)

        while("N" in string):
            ret += "9"
            string = re.sub("N(.*)","\\1",string)
            string = re.sub("I(.*)","\\1",string)
            string = re.sub("N(.*)","\\1",string)
            string = re.sub("E(.*)","\\1",string)
    ret = sorted(ret)
    reti = ""
    while ret:
        reti += ret[0]
        ret.pop(0)

    print("Case #{}: {}".format(case + 1,reti))
