__author__ = 'Hp Pc'

inputFile = open("input.txt", 'r');
outputFile = open("output.txt", 'w');
count = int(inputFile.readline());
lineno = 1;

while lineno <= count:
    inp = inputFile.readline().split();
    tileCount = int(inp[0]);
    complexity = int(inp[1]);
    minimum = int(inp[2]);
    if minimum==tileCount:
        ans="";
        tt=1;
        while tt<=pow(tileCount,complexity):
            ans=ans+" "+str(tt);
            tt=tt+pow(tileCount,complexity-1);
        line = "Case #" + `lineno` + ": " +ans.lstrip() + "\n";
        outputFile.write(line);
        lineno = lineno + 1;
        continue;
    tiles = [0]*tileCount;
    permutations=[];
    while True:
        temp = tiles [:]
        for i in range(1,complexity):
            j=0;
            while j < tiles.__len__():
                if tiles[j]==0:
                    tiles= tiles[:j]+temp+tiles[j+1:];
                else:
                    tiles =tiles[:j]+[1]*temp.__len__()+tiles[j+1:];
                j=j+temp.__len__();

        permutations.append(tiles[:]);
        tiles=temp;
        if tiles.__contains__(0)==False:
            break;
        for j in range(0,tiles.__len__()):
            if tiles[j]==1:
                tiles[j]=0
            else:
                tiles[j]=1;
                break;
    trial =[0]*permutations[0].__len__();
    answer="";
    for t in range(1,permutations[0].__len__()+1):
        answer=answer+" "+str(t);
    min=permutations[0].__len__();
    while True:
        countvar=0;
        content=[];
        var="";
        for j in range(0,permutations[0].__len__()):
            if trial[j]==1:
                countvar=countvar+1;
                var=var+" "+str(j+1);
                for k in range(0,permutations.__len__()):
                    if permutations[k][j]==1:
                        if content.__contains__(k)==False:
                            content.append(k);
        if content.__len__()==permutations.__len__()-1:
            if countvar<min:
                answer=str(var);
                min=countvar;
        while True:
            if trial.__contains__(0)==False:
                break;
            for j in range(0,trial.__len__()):
                if trial[j]==1:
                    trial[j]=0
                else:
                    trial[j]=1;
                    break;
            if trial.count(1)<min:
                break;
        if trial.__contains__(0)==False:
            break;
    if minimum<min:
        line = "Case #" + `lineno` + ": " +"IMPOSSIBLE" + "\n";
    else:
        line = "Case #" + `lineno` + ": " +answer.lstrip() + "\n";
    outputFile.write(line);
    lineno = lineno + 1;
inputFile.close();
outputFile.close();
