#problem A

fname = "test"
inf = open(fname, 'r')
ofname = "test_output"
of = open(ofname, 'w')

i=0;

for line in inf:
    if(i==0):
        T = int(line);
        i = i+1;
    else:
        if(i>1):
            of.write("\n");
        of.write("Case #"+ str(i) + ": ");
        i = i+1;
        N = int(line);
        if(N==0):
            of.write("INSOMNIA");
        else:
            num_a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
            count = 0;
            ln = N; 
            j = 1;
            while(count<10):
                #check digits seen
                ln = j*N;
                n = ln;
                while(n>=1):
                    d = n%10;
                    n = n/10;
                    if(num_a[d]==0):
                        count = count+1;
                        num_a[d] = 1;
                    if(count==10):
                        break;
                j = j+1;
            of.write(str(ln));
inf.close();
of.close();