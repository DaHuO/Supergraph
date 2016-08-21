f = open('A-large.in', 'r');
f2 = open('resultLarge.txt', 'w');

T = f.readline();



for i in range(0, int(T)):
    line = f.readline();
    line = line.rstrip('\n');
    done = False;
    mulcount = 2;
    N = int(line);
    mul = N;
    letterCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    countout = 0;
    while countout < 100:
        numstring = str(mul);
        for letter in numstring:
            num = int(letter);
            letterCount[num] += 1;
            
        #print letterCount;

        done = True;
        for el in letterCount:
            if el == 0:
                done = False;
                break;

        if done:
            #print "N:" + str(N);
            f2.write("Case #" + str(i+1) + ": " +str(mul) + '\n');
            break;

        prevMul = mul;
        
        mul = N * mulcount;

        if (mul == prevMul):
            f2.write("Case #" + str(i+1) + ": INSOMNIA\n");
            break;
            
        #print "mul:" + str(mul);
        mulcount += 1;

        countout += 1;
         
f.close();
f2.close();
