
counter = 0


def flip(panc):
    panc = panc.replace("+", "o")
    panc = panc.replace("-", "x")
    panc = panc.replace("o", "-")
    panc = panc.replace("x", "+")
    return panc

def count_mane(panc, counter,c):    
    a = panc.find("-")
    if(a == -1):
        answer = "Case #{0}: {1}\n".format(c, counter)
        f = open("out.txt", "a")
        f.write(answer)
        f.close()
        return counter
    else:
        panc = panc[a:len(panc)]
        panc = flip(panc)
        counter += 1
        count_mane(panc, counter, c)
        


def main():
    c = 0
    fil = open("in.txt", "r")
    for line in fil:
        if( c == 0):
            T = line
            T = int(T)
        else:
            line = line[::-1]
            count_mane(line, counter, c)

        c += 1
        counter = 0
    fil.close()
            
main()
