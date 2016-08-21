Tc = int(input())
for t in range(1,Tc + 1):
    S = input()
    alph = {}
    accepted = ['Z','O','W','H','U','V','X','S','G','I']
    phone = [0]*10
    for c in S:
        if c in accepted:
            if c in alph:
                alph[c]+=1
            else:
                alph[c] = 1
    phone[0] = alph['Z'] if 'Z' in alph else 0
    phone[2] = alph['W'] if 'W' in alph else 0
    phone[6] = alph['X'] if 'X' in alph else 0
    phone[8] = alph['G'] if 'G' in alph else 0
    phone[4] = alph['U'] if 'U' in alph else 0
    phone[7] = (alph['S'] - phone[6])if 'S' in alph else 0
    phone[5] = (alph['V'] - phone[7])if 'V' in alph else 0
    phone[3] = (alph['H'] - phone[8])if 'H' in alph else 0
    phone[1] = (alph['O'] - phone[0] - phone[2] - phone[4])if 'O' in alph else 0
    phone[9] = (alph['I'] - phone[5] - phone[6] - phone[8])if 'I' in alph else 0

    ans=''
    for i,v in enumerate(phone):
       ans+=str(i)*v 
    print("Case #{0}: {1}".format(t,ans))