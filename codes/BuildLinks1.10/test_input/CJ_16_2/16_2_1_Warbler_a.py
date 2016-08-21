import sys

def solve(s):
    m_s={}
    m_s["Z"]=0
    m_s["O"]=0
    m_s["N"]=0
    m_s["E"]=0
    m_s["T"]=0
    m_s["W"]=0
    m_s["H"]=0
    m_s["R"]=0
    m_s["F"]=0
    m_s["O"]=0
    m_s["R"]=0
    m_s["U"]=0
    m_s["F"]=0
    m_s["I"]=0
    m_s["V"]=0
    m_s["E"]=0
    m_s["S"]=0
    m_s["I"]=0
    m_s["X"]=0
    m_s["S"]=0
    m_s["E"]=0
    m_s["V"]=0
    m_s["E"]=0
    m_s["N"]=0
    m_s["E"]=0
    m_s["I"]=0
    m_s["G"]=0
    m_s["H"]=0
    m_s["T"]=0
    m_s["N"]=0
    m_s["I"]=0
    m_s["N"]=0
    m_s["E"]=0
    for i in range(len(s)): #EGHFXTOURIST
        if m_s.has_key(s[i])==True:
            m_s[s[i]]=m_s[s[i]]+1
        else:
            m_s[s[i]]=1
    rst=[]
#"ZERO" "TWO" "SIX" "SEVEN" "EIGHT" "FOUR" "ONE"
#, , , "THREE", , "FIVE", , , , "NINE"
    while m_s["Z"]>0:
        rst.append(0)
        m_s["Z"]=m_s["Z"]-1
        m_s["E"]=m_s["E"]-1
        m_s["R"]=m_s["R"]-1
        m_s["O"]=m_s["O"]-1
    while m_s["W"]>0:
        rst.append(2)
        #rst=rst+"2"
        m_s["T"]=m_s["T"]-1
        m_s["W"]=m_s["W"]-1
        m_s["O"]=m_s["O"]-1
    while m_s["X"]>0:
        rst.append(6)
        #rst=rst+"6"
        m_s["S"]=m_s["S"]-1
        m_s["I"]=m_s["I"]-1
        m_s["X"]=m_s["X"]-1
    while m_s["S"]>0:
        rst.append(7)
        #rst=rst+"7"
        m_s["S"]=m_s["S"]-1
        m_s["E"]=m_s["E"]-1
        m_s["V"]=m_s["V"]-1
        m_s["E"]=m_s["E"]-1
        m_s["N"]=m_s["N"]-1
    while m_s["G"]>0:
        rst.append(8)
        #rst=rst+"8"
        m_s["E"]=m_s["E"]-1
        m_s["I"]=m_s["I"]-1
        m_s["G"]=m_s["G"]-1
        m_s["H"]=m_s["H"]-1
        m_s["T"]=m_s["T"]-1
    while m_s["U"]>0:
        rst.append(4)
        #rst=rst+"4"
        m_s["F"]=m_s["F"]-1
        m_s["O"]=m_s["O"]-1
        m_s["R"]=m_s["R"]-1
        m_s["U"]=m_s["U"]-1
    while m_s["O"]>0:
        rst.append(1)
        #rst=rst+"1"
        m_s["E"]=m_s["E"]-1
        m_s["N"]=m_s["N"]-1
        m_s["O"]=m_s["O"]-1

    while m_s["T"]>0:
        rst.append(3)
        #rst=rst+"3"
        m_s["T"]=m_s["T"]-1
        m_s["H"]=m_s["H"]-1
        m_s["R"]=m_s["R"]-1
        m_s["E"]=m_s["E"]-1
        m_s["E"]=m_s["E"]-1

    while m_s["F"]>0:
        rst.append(5)
        #rst=rst+"5"
        m_s["F"]=m_s["F"]-1
        m_s["I"]=m_s["I"]-1
        m_s["V"]=m_s["V"]-1
        m_s["E"]=m_s["E"]-1

    while m_s["N"]>1:
        rst.append(9)
        #rst=rst+"9"
        m_s["N"]=m_s["N"]-1
        m_s["I"]=m_s["I"]-1
        m_s["N"]=m_s["N"]-1
        m_s["E"]=m_s["E"]-1
    rst.sort()
    str1="".join(str(x) for x in rst)
    return str1

f_input=open(sys.argv[1])
testcases=int(f_input.readline().rstrip())
for caseNr in xrange(1, testcases+1):
    s=f_input.readline()
    s=s.rstrip()
    print("Case #%s: %s" % (caseNr, solve(s)))
f_input.close()