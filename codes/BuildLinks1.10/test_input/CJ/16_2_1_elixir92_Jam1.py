__author__ = 'Hp Pc'
__author__ = 'Hp Pc'

inputFile = open("input.txt", 'r');
outputFile = open("output.txt", 'w');
count = int(inputFile.readline());
lineno = 1;

while lineno <= count:
    number = [];
    str = inputFile.readline().rstrip();
    str = list(str);
    iter = 0;
    str.sort();
    while iter < len(str):
        if (str!=[] and str[iter] == 'Z'):
            str.remove('Z');
            str.remove('E');
            str.remove('R');
            str.remove('O');
            iter = iter - 4;
            number.append(0)
        if (str!=[] and str[iter] == 'W'):
            str.remove('W');
            str.remove('T');
            str.remove('O');
            iter = iter - 3;
            number.append(2)
        if (str!=[] and str[iter] == 'U'):
            str.remove('U');
            str.remove('F');
            str.remove('O');
            str.remove('R');
            iter = iter - 4;
            number.append(4)
        if (str!=[] and str[iter] == 'X'):
            str.remove('X');
            str.remove('S');
            str.remove('I');
            iter = iter - 3;
            number.append(6)
        if (str!=[] and str[iter] == 'G'):
            str.remove('G');
            str.remove('E');
            str.remove('I');
            str.remove('H');
            str.remove('T');
            iter = iter - 2;
            number.append(8);
        iter = iter + 1;

    iter = 0;
    while iter < len(str):
        if (str!=[] and str[iter] == 'O'):
            str.remove('O');
            str.remove('N');
            str.remove('E');
            iter = iter - 3;
            number.append(1);
        if (str!=[] and str[iter] == 'H'):
            str.remove('H');
            str.remove('T');
            str.remove('R');
            str.remove('E');
            str.remove('E');
            iter=iter-3;
            number.append(3)
        if (str!=[] and str[iter] == 'F'):
            str.remove('V');
            str.remove('F');
            str.remove('I');
            str.remove('E');
            iter = iter - 2;
            number.append(5)
        if (str!=[] and str[iter] == 'S'):
            str.remove('S');
            str.remove('E');
            str.remove('V');
            str.remove('E');
            str.remove('N');
            iter = iter - 4;
            number.append(7)
        iter = iter + 1;
    iter = 0;
    while iter < len(str):
        if (str!=[] and str[iter] == 'I'):
            str.remove('I');
            str.remove('N');
            str.remove('E');
            str.remove('N');
            iter = iter - 2;
            number.append(9);
        iter = iter + 1;

    number.sort();
    ans=""
    for iter in number:
        ans=ans+`iter`;
    line = "Case #" + `lineno` + ": " +ans+"\n";
    outputFile.write(line);
    print(line)
    lineno = lineno + 1;
inputFile.close();
outputFile.close();
