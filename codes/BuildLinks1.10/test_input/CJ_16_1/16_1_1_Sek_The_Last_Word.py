#! python3
cases=int(input())
left=[]; right=[]; m_letter='A';

for case in range(1,cases+1):
    S_list=list(input().strip())
    left=[];right=[]; m_letter='A';

    for letter in S_list:
        if letter<m_letter:
            right.append(letter)
        else:
            left.append(letter)
            m_letter=letter

    left=left[::-1]
    word=''.join(left+right)
    
    print('Case #{}: {}'.format(case, word))