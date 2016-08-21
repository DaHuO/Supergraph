def digits(num, blist):
        while num != 0:
            blist[num % 10] = True
            num = num / 10  
        return blist

inn = open("inn.txt")
out = open("out.txt", 'w')
T = int(next(inn))
for i in range(T):
        N = int(next(inn))
        Ni = N
        diglist = digits(Ni, [False]*10)
        if N == 0:
                out.write("Case #" + str(i + 1) + ": INSOMNIA\n")
        else:
                while not all(diglist):
                        Ni = Ni + N 
                        diglist = digits(Ni,diglist)
                out.write("Case #" + str(i + 1) + ": " + str(Ni) + "\n")
inn.close()
out.close()
