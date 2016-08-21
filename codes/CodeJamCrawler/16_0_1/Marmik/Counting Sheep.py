cases = int(input());
for i in range(cases):
    number = int(input());
    if number == 0 :
        print("Case #",i+1,": INSOMNIA", sep='');
        continue;
    digitsSeen = [];
    n = 1;
    while(len(digitsSeen)<10) :
        letStr = str(number * n);
        for l in letStr :
            if int(l) not in digitsSeen :
                digitsSeen.append(int(l));
        n+=1;
    print("Case #",i+1,": ", (n-1)*number, sep='');
