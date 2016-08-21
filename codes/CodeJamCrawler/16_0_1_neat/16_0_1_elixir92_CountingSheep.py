__author__ = 'Hp Pc'

inputFile = open("input.txt", 'r');
outputFile = open("output.txt", 'w');
count = int(inputFile.readline());
lineno = 1;

while lineno <= count:
    iter = 1;
    num = int(inputFile.readline());
    current = num;
    track = [False] * 10;
    numTrack = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

    while True:
        if num == 0:
            break;
        current = iter * num;
        iter = iter + 1;
        temp = current;
        while temp != 0:
            track[temp % 10] = True;
            temp = temp / 10;
        iter_1 = 0;
        while iter_1 < numTrack.__len__():
            if track[numTrack[iter_1]] == True:
                numTrack.remove(numTrack[iter_1]);
            else:
                iter_1 = iter_1 + 1;
        if numTrack.__len__() == 0:
            break;
    if num == 0:
        line = "Case #" + `lineno` + ": " + "Insomnia" + "\n";
    else:
        line = "Case #" + `lineno` + ": " + `current` + "\n";
    outputFile.write(line);
    lineno = lineno + 1;
inputFile.close();
outputFile.close();
