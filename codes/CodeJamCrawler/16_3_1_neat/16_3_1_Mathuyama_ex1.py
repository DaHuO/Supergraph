import numpy as np

# //////////////////////// PARSER /////////////////////////////

def getInfo(line):
    t = []
    for n in line.split(' '):
        t.append(n)
    return t

def parse(path):
    file = open(path,"r");
    nbCases = int(file.readline());
    txt = file.readlines();
    cases = []
    for line in txt:
        cases.append(getInfo(line));
    file.close()
    return cases

# /////////////////////////// WORK //////////////////////////////

def work(t):
    steps=[]
    N = int(t[0][0]);
    S = [int(t[1][i]) for i in range(len(t[1]))]
    counter = 0;
    for x in S:
        counter+=x;
    while (counter>0):
        step = []
        detect = 0
        for i in range(N):
            toast = (counter-(detect+1))/2;
            if detect < 2:
                if S[i]>toast:
                    if(S[i]-1)>toast:
                        S[i]-=2
                        step.append(i)
                        step.append(i)
                        detect += 2
                    else:
                        S[i]-=1
                        step.append(i)
                        detect += 1
        if detect == 0:
            i = 0;
            while (S[i] == 0):
                i+=1
            S[i]-=1
            step.append(i)
        steps.append(step)
        counter-=len(step)

    string = ""
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for s in steps:
        for i in range(len(s)):
            string+=abc[s[i]]
        string+=' '
    return string
    

# //////////////////// MAIN //////////////////////////////////


def createOutput(data,path):
    file = open(path,'w');
    count = 0;
    for i in range(0,len(data),2):
        R = work([data[i],data[i+1]]);
        count += 1;
        file.write("Case #"+str(count)+": "+R+"\n");
    file.close();

def main(txtInput,txtOutput):
    data = parse(txtInput);
    createOutput(data,txtOutput);
    

main("A-large(1).in","outputattempt.out");
