SUSHU = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997)

def doit(str_line):
    i = len(str_line) - 1;
    ans = 0;
    while(1):
        if(str_line[i] == '-'):
            break;
        if(i == 0):
            return 0;
        i -= 1;
    
    i -= 1;
    ans += 1;
    while(i >= 0):
        if(str_line[i] != str_line[i + 1]):
            ans += 1;
        i -= 1;  
    return ans;

def if_heshu(num):
    for i in SUSHU:
        if(num%i==0):
            return i;
    return -1;
        
        
                



file_in = open("in.txt", 'r+');
file_out = open("out.txt", 'w+');
file_out.write('Case #1:\n');


ARR = [[0]*33]*20;
for i in range(2, 11):
    ARR[i] = [i**x for x in range(0, 33)];
    

# number = [ARR[i][15] + 1 for i in range(2, 10)];
NUM = (1 << 31) + 1;
print(NUM & (1 << 0))
for haha in ARR:
    print(haha)
    
ANS = 0;

while(ANS < 500):
    printoo = [0]*11;
    for radix in range(2, 11):
        number = 0;
        for i in range(0, 32):
            if(NUM & (1 << i)):
                number += ARR[radix][i];
#                 file_out.write(str(NUM)+' '+str(number)+'\n');
        printoo[radix] = if_heshu(number);
        if(printoo[radix] == -1):
            break;    
    else:
        file_out.write('{0:b}'.format(NUM));
        for radix in range(2, 11):
            file_out.write(' %d' % (printoo[radix]));
        file_out.write('\n');
        ANS += 1;      
    NUM += 2;
file_out.close();
        
    
