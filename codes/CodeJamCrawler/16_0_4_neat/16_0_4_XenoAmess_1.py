def get_now_index(old_index, K, C):
    old_index -= 1;
    res = old_index;
    t = 0;
    while(t < C-1):
        t += 1;
        res *= K;
        res += old_index;
    return res + 1;  
                



file_in = open("in.txt", 'r+');
file_out = open("out.txt", 'w+');
T = int(file_in.readline());
t = 0;
while(1):
    lines = file_in.readlines(100000);
    if not lines:
        break;
    for line in lines:
        
        K, C, S = line.split(' ');
        
        K = int(K);
        C = int(C);
        S = int(S); 
        t += 1;
        file_out.write('Case #%d:' % (t,));
        lanlan = [get_now_index(i, K, C) for i in range(1, S + 1)];
        for num in lanlan:
             file_out.write(' %d' % (num,));
        file_out.write('\n');   
file_in.close();
file_out.close();
        
    
