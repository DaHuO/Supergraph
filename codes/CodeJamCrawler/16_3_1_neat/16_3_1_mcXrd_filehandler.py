



def Write(filename,lines):
    with open('C:\\codejam\\'+filename, "w") as file:
        for one in lines:
            file.write(str(one)+'\n')



def Read(filename):
    ret = []
    with open('C:\\codejam\\'+filename, "r") as file:
        for one in file:
            t = one.replace('\n','')
            ret.append(t)
    return ret