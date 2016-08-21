fin = open('A-large.in', 'r');
fout = open('sheep.out', 'w');
N = int(fin.readline());

for i in range(N):
    count = int(fin.readline());
    forever = False;
    last = -1;
    if(count == 0):
        forever = True;
    if not forever:
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
        counter = 1;
        while True:
            new = count * counter;
            for char in str(new):
                if char in nums:
                    nums.remove(char);
            if (len(nums) == 0):
                last = new;
                break;
            counter += 1;
    
    if forever:
        fout.write('Case #'+str(i+1)+': INSOMNIA\n');
    else:
        fout.write('Case #'+str(i+1)+': '+str(last)+'\n');

fin.close();
fout.close();
