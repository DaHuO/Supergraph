
def parse(path):
    files = open(path)
    files.readline()
    content = files.readlines()
    return content
    
def lastWord(word):
    res = word[0]
    for i in range(1,len(word)):
        if (word[i] < res[0]):
            res = res+word[i]
        else:
            res = word[i]+res
    return res

print (lastWord("abab"))

def output():
    data=(parse("A-large.in"))
    L = []
    for i in range(len(data)):
        L.append("Case #"+str(i+1)+": "+lastWord(data[i]))
    output=(open("outputword.out","w"))
    output.writelines(L)

output()
