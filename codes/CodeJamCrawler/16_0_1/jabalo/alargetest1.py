f = open('/Users/jacquelineabalo/Documents/A-large.in');
lines = f.readlines();

for i in range(1, len(lines)):
    seen = [0,0,0,0,0,0,0,0,0,0];
    tsum = 0;
    N = lines[i];
    N = N.strip();
    N = int(N);
    if N==0:
        print('Case #' + str(i) + ': ' + 'INSOMNIA');
    else:
        initial = N;
        while tsum!=10:
            NStr = str(N);
            for j in NStr:
                jInt = int(j);
                if seen[jInt]==0:
                    tsum = tsum + 1; 
                seen[jInt]=1;
            N = N + initial;
        print('Case #' + str(i) + ': ' + str(N-initial));
            
        
    
