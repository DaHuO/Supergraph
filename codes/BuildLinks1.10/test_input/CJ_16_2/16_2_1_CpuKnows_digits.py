import re
import numpy as np

ZERO = list('ZERO') #unique
ONE = list('ONE')
TWO = list('TWO') #unique
THREE = list('THREE')
FOUR = list('FOUR')
FIVE = list('FIVE')
SIX = list('SIX') #unique
SEVEN = list('SEVEN')
EIGHT = list('EIGHT') #unique
NINE = list('NINE')


g = open('D:\Users\john\My Documents\Google Code Jam\Google Code Jam 2016\digits\small_out.txt','w+')

with open('D:\Users\john\My Documents\Google Code Jam\Google Code Jam 2016\digits\A-small-attempt1.in', 'r+') as f:
    num_cases = int(f.readline())
    
    for i in range(num_cases):
        # Unique: g, eight; w, two; x, six; z, zero;
        phone_str = list(f.readline())
        if(phone_str[-1] == '\n'):
            phone_str = phone_str[0:-1]
        phone_num = []
        count = 0
        
        while(len(np.intersect1d(ZERO, phone_str)) == 4):
            # Zero
            for letter in ZERO:
                phone_str.remove(letter)
            phone_num.append(0)
        
        while(len(np.intersect1d(TWO, phone_str)) == 3):
            # Two
            for letter in TWO:
                phone_str.remove(letter)
            phone_num.append(2)
        
        while(len(np.intersect1d(SIX, phone_str)) == 3):
            # Six
            for letter in SIX:
                phone_str.remove(letter)
            phone_num.append(6)
            
        while(len(np.intersect1d(EIGHT, phone_str)) == 5):
            # Eight
            for letter in EIGHT:
                phone_str.remove(letter)
            phone_num.append(8)
            
        while(len(np.intersect1d(SEVEN, phone_str)) == 4 and 
              phone_str.count('E') >= 2):
            # Seven
            for letter in SEVEN:
                phone_str.remove(letter)
            phone_num.append(7)
            
        while(len(np.intersect1d(FIVE, phone_str)) == 4):
            # Five
            for letter in FIVE:
                phone_str.remove(letter)
            phone_num.append(5)
            
        while(len(np.intersect1d(FOUR, phone_str)) == 4):
            # Four
            for letter in FOUR:
                phone_str.remove(letter)
            phone_num.append(4)
        
        while(len(np.intersect1d(THREE, phone_str)) == 4 and
              phone_str.count('E') >= 2):
            # Three
            for letter in THREE:
                phone_str.remove(letter)
            phone_num.append(3)
            
        while(len(np.intersect1d(NINE, phone_str)) == 3 and
              phone_str.count('N') >= 2):
            # Nine
            for letter in NINE:
                phone_str.remove(letter)
            phone_num.append(9)
            
        while(len(np.intersect1d(ONE, phone_str)) == 3):
            # One
            for letter in ONE:
                phone_str.remove(letter)
            phone_num.append(1)
        
        phone_num.sort()
        phone_num = ''.join([str(x) for x in phone_num])
        
        if(len(phone_str) != 0):
            print(str(i), phone_str, phone_num)
        
        g.write('Case #' + str(i+1) + ': ' + str(phone_num) + '\n')
        
g.close()