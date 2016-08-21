import time

patates = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0

}




def number_checker(counter):
    for x in counter:
        if(counter[x] == 0):
            return False
    return True

def number_processor(N, counter):
    
    while(N != 0):
        a = N % 10
        counter[ a ] += 1
        N = int(N/10)

def test_each(N, x):
    c = 1
    while(True):
        if(N == 0):
            answer = "Case #{0}: {1}\n".format(x, "INSOMNIA")
            f = open("out.txt", "a")
            f.write(answer )
            f.close()
            break
        A = c*N
        number_processor(A, patates)
        if( number_checker(patates) == True):
            answer = "Case #{0}: {1}\n".format(x, A)
            f = open("out.txt", "a")
            f.write(answer )
            f.close()
            print(A)
            for i in patates:
                patates[i] = 0
            break
        c = c + 1
    
    


def main():
    x = 0
    fil = open("in.txt", "r")
    for line in fil:
        if(x == 0):
            N = line
            N = int(N)
        else:
            test_each(int(line), x)

        x += 1
    fil.close()

main()
            
    



        
    
