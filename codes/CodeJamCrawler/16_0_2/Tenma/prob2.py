#------------------------------- problem 2 ---------------------------------
def flipcake(cake):
    piece = cake[0];
    count = 0;
    for i in range (1,len(cake)-1):
        if (cake[i]!=piece):

            count+=1;
            piece =cake[i];

    if (piece == '-'):
        count +=1;

    return count;

if __name__ == '__main__':

    f = open('B-small-attempt2.in', 'r');

    t = int(f.readline());

    for i in range(t):
        prt = "Case #"+str(i+1)+": ";
        cake = f.readline();

        res = flipcake(cake);

        prt += str(res);
        print prt
    
