__author__ = 'Hp Pc'

inputFile = open("input.txt", 'r');
outputFile = open("output.txt", 'w');
count = int(inputFile.readline());
lineno = 1;

while lineno <= count:
    pancakes = list(inputFile.readline().strip("\n"));
    current = pancakes[0];
    trials = 0;
    if current == '-':
        next = '+';
    else:
        current = '+';
        next = '-';

    iter = 0;
    while True:
        while iter < pancakes.__len__():
            if pancakes[iter] != current:
                break;
            else:
                pancakes[iter] = next;
            iter = iter + 1;
        trials = trials + 1;
        temp = current;
        current = next;
        next = temp;
        if iter == pancakes.__len__():
            break;
        iter = 0;

    if pancakes[pancakes.__len__() - 1] == '-':
        trials = trials - 1;

    line = "Case #" + `lineno` + ": " + `trials` + "\n";
    outputFile.write(line);
    lineno = lineno + 1;

inputFile.close();
outputFile.close();
