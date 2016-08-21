file = open("A-large.in","r")
contents = file.readlines()
numbers = contents[0].strip()
inputs = [contents[i].strip() for i in range(1,int(numbers)+1)]
results = []

def last_word(x):
    lastwordlist = []
    wordlist = list(str(x))
    lastword = wordlist[0]
    for i in range (len(wordlist)-1):
        if lastword[0] > wordlist[i+1]:
            lastword = lastword + wordlist[i+1]
        else:
            lastword = wordlist[i+1] + lastword
    
    return lastword

for n in inputs:
    results.append(last_word(n))

file.close()

file = open("A-large.out","w")

for a in range(len(results)):
    file.write("Case #{0}: {1}\n".format(a+1,results[a]))
file.close()



        
        
        
        
    
