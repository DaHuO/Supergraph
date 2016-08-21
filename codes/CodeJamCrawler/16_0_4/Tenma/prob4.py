#---------------------- problem 4 - small ---------------------


def countLG(k,c,s):
    res = "";

    if (s == k):
            for i in range(k):
                res = res + " " + str(i+1);

            return res;
    else:
        return "UNSOLVED";


if __name__ == '__main__':

    f = open('test.txt', 'r');

    t = int(f.readline());

    for i in range(t):
        prt = "Case #"+str(i+1)+":";

        line = f.readline();

        line = line.split();

        k = int(line[0]);
        c = int(line[1]);
        s = int(line[2]);

        res = countLG(k,c,s);

        prt +=res;

        print prt
    
