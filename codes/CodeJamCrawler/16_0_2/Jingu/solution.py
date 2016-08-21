#problem B

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
        count = 0;
        prev_c = line[0]
        for cur_c in line:
            if(cur_c=='\n'):
                break;
            if(cur_c!=prev_c):
                count = count+1
            prev_c = cur_c
        if(prev_c=='-'):
            count = count + 1;
        of.write(str(count))
    if(i>T):
        break;
        
inf.close();
of.close();        