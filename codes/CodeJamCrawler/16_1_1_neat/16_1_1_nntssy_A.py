def getWinWord(S):
    winWord=S[0]
    for i in range(1,len(S)):
        if S[i]<winWord[0]:
            winWord+=S[i]
        else:
            winWord=S[i]+winWord
    return winWord       

def main(fin,fout):
    numCases=int(fin.readline())
    for i in range(numCases):
        case=fin.readline().strip()
        fout.write('Case #'+str(i+1)+': '+getWinWord(case)+'\n')
        
fin=open('C:\Users\exin1\Google Drive\Study\Google CodeJam\Round 1A\A.in','r')
fout=open('C:\Users\exin1\Google Drive\Study\Google CodeJam\Round 1A\A.out','w')
main(fin,fout)
fin.close()
fout.close()