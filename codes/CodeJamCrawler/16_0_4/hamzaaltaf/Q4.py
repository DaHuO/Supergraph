fo = open("D-small-attempt01.in", "r")
writefile = open('Q4.txt','w');
counter = 0;
alist = [];
b = []; sleep = 0;
answers = [];
n =1;
length = 0;
a= ['0','1','2','3','4','5','6','7','8','9'];
for line in fo:
    counter +=1
    if counter ==1:
        total = line;
        #print ('THis total',total);
    else:
        line = line.strip();
        line = str(line);
        line = line.split()
        print(line);
        length = len(line)-1;
        for i in range(0,length):
            if (int(line[i])) == (int(line[length])):
                number = int(line[0]);
                print('This is number',number);
                writefile.write('Case #{0}: '.format(n));n=n+1;
                for i in range(1,number+1):
                    print('this is i',i);
                    writefile.write(str(i));writefile.write(' ');
                writefile.write('\n');
                break;
            elif(int(line[0]))<int(int(line[length])):
                writefile.write('IMPOSSIBLE');
                writefile.write('\n');
