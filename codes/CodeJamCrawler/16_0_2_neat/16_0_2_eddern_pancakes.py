
def count(seq):
    teller = 0
    current = seq[0]
    for i in seq:
        if not i == current:
            teller += 1
            current = i
    if seq[-1] == "-":
        teller += 1
    return teller


def main():
    fil = open('B-large.in','r')
    output = open('output.txt','w')
    cases = fil.readline()
    for i in range(int(cases)):
        seq = fil.readline()
        if not i-1 == int(cases):
            seq = seq[:len(seq)-1]
        svaret = count(seq)
        print("Case #"+str(i+1)+": "+str(svaret))
        output.write("Case #"+str(i+1)+": "+str(svaret)+"\n")
    output.close()
    fil.close()


main()
