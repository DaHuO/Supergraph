def main():
    solve()

import sys
def solve():
    data = sys.stdin.readlines()
    trials = data[0]
    for i in range(1, len(data)):
        print("Case #" + str(i) + ": " + str(ans(int(data[i]))))

def ans(num):
    numbers = [1,2,3,4,5,6,7,8,9,0]
    if num == 0:
        return 'INSOMNIA'
    else:
        i=1
        while numbers: 
            for digit in str(i * num):
                try:
                    numbers.remove(int(digit))
                except:
                    pass
            i+=1
        return (i-1)*num
    

if __name__ == "__main__":
    main()

