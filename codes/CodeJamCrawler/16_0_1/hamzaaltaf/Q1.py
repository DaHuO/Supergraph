fo = open("A-large.in", "r")
counter = 0;
alist = [];
b = []; sleep = 0;
answers = [];
a= ['0','1','2','3','4','5','6','7','8','9'];
for line in fo:
    counter +=1
    if counter ==1:
        total = line;
        #print ('THis total',total);
    else:
        line = line.strip();
        line = int(line);
        for anotherCounter in range(1,200):
            #print('This is the another counter',anotherCounter)
            result = line*anotherCounter;
            array = str(result);
            for i in array:
                alist.append(i);
            b = list(set(alist));
            b = sorted(b);
            if a == b:
                print(result);
                answers.append(result);
                sleep = 1;
                break;
        alist[:]=[];
        if sleep==0:
            print('Insomia');
            answers.append('INSOMNIA');
with open('output.txt', 'w') as f:
    case_number = 1
    for n in answers :
        f.write('Case #{0}: {1}\n'.format(case_number, n))
        case_number += 1
