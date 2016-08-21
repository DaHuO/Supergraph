
file_in = open("in.txt",'r+');
file_out = open("out.txt",'w+');

def doit(str_line):
    ary_ifnums = 0;
    if(not str_line.isdigit()):
        str_line = str_line[:-1];
    
    int_N = int(str_line);
    str_N = str_line;
    rn = 0;
    
    while(1):
        rn+=1;
        for chr_c in str_N:
            ary_ifnums = (ary_ifnums | (1 << int(chr_c)));
        if (ary_ifnums == (1 << 10) - 1):
            return str_N;
        elif(rn>1000):
            return 'INSOMNIA';
        else :
#             print(str_N);
            str_N = str(int(str_N) + int_N);





T = int(file_in.readline());
t = 0;
while(1):
    lines = file_in.readlines(100000);
    if not lines:
        break;
    for line in lines:
        t += 1;
        file_out.write('Case #%d: %s\n' % (t, doit(line)));
    
file_in.close();
file_out.close();
        
    
