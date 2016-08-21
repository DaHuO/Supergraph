import itertools

unique_digit_even = {'Z':'0','W':'2','U':'4','X':'6','G':'8'}
unique_digit_odd = [('O','1'),('H','3'),('F','5'),('S','7'),('N','9')]
unique_num = {'Z':'ZERO','W':'TWO','U':'FOUR','X':'SIX','G':'EIGHT','O':'ONE','H':'THREE','F':'FIVE','S':'SEVEN','N':'NINE'}


def get_phone(s):
    res = ''

    # even
    
    for i in unique_digit_even:
        while True:
            if i in s:
                res = res + unique_digit_even[i]
                for char in unique_num[i]:
                    s = s.replace(char,'',1)
            else:
                break

    # odd
    for i in unique_digit_odd:
        j = i[0]
        while True:
            if j in s:
                res = res + i[1]
                for char in unique_num[j]:
                    s = s.replace(char,'',1)
            else:
                break
    
    return ''.join(sorted(res))
    
    

testcases = int(input())

for tc in range(1,testcases+1):
    s = input()
    print('Case #',tc,': ',get_phone(s),sep='')
