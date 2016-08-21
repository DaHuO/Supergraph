def fname(S):
    let = [0]*26
    for item in S:
        let[ord(item)-65]+=1
    N = [0]*10
    N[0]=let[ord('Z')-65]
    N[6]=let[ord('X')-65]
    N[2]=let[ord('W')-65]
    N[8]=let[ord('G')-65]
    N[4]=let[ord('U')-65]
    N[3]=let[ord('R')-65]-N[0]-N[4]
    N[5]=let[ord('F')-65]-N[4]
    N[7]=let[ord('V')-65]-N[5]
    N[1]=let[ord('O')-65]-N[0]-N[2]-N[4]
    N[9]=let[ord('I')-65]-N[5]-N[6]-N[8]
    number = ''
    for i in range(10):
        number += str(i)*N[i]
    return number

t = int(input())
for i in range(1, t + 1):
    s= input()
    print("Case #{}: {}".format(i, fname(s)))
