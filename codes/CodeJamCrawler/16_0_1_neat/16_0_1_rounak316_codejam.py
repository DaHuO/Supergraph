

with open("C:\\Users\\prakhar\\Downloads\\A-large.in") as f:
    lines = f.readlines()

def input():
    return lines.pop(0)

def fun(N , no):

    if N == 0:
        return "INSOMNIA"

    M=1
    P=N

    while True:

        if len(no)==0:
            return str(tmp)

        tmp = M*N
        M=M+1
        for char in str(tmp):
            try:
                no.remove((char))
            except:
                pass



T=(int)(input())
NO = [char for char in str('0123456789')]
OUTPUT = ''

for i in range(T):
    no = list(NO)
    N =(int)(input())
    OUT =  fun(N , no)
    OUTPUT += ("Case #" +str(i+1) + ": " + OUT + "\n")

print(OUTPUT)
with open("OUT.out" , 'w') as f:
    f.write(OUTPUT)
