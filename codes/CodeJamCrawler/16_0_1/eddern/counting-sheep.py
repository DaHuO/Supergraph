def countSheep(n):
    queue = [0,1,2,3,4,5,6,7,8,9]
    tall = 0
    if(n == 0):
        return 0
    while queue:
        tall += n
        for num in str(tall):
            if int(num) in queue:
                queue.remove(int(num))
    return tall

def main():
    fil = open('A-large.in','r')
    output = open('output.txt','w')
    cases = fil.readline()
    for i in range(int(cases)):
        tallet = fil.readline()
        svaret = countSheep(int(tallet))
        if svaret == 0:
            print("Case #"+str(i+1)+": INSOMNIA")
            output.write("Case #"+str(i+1)+": INSOMNIA\n")
        else:
            print("Case #"+str(i+1)+": "+str(svaret))
            output.write("Case #"+str(i+1)+": "+str(svaret)+"\n")
    output.close()
    fil.close()


main()
