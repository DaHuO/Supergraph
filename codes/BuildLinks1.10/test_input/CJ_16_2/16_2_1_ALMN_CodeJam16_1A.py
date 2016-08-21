import os

case_num = 1

def string_sorter(string):
    return ''.join(sorted(string))
                    #1  3   5    7  9   11  13  15   17 19  21   23  25  27  29
possible_letters = ['E','F','G','H','I','N','O','R','S','T','U','V','W','X','Z']

def counting_thingy(string):
    total_counts = []
    for letter in possible_letters:
        t = string.count(letter)
        total_counts.append(letter)
        total_counts.append(t)
    return total_counts

def numbermaker(string):
    phonenum = ''
    while string[29] > 0:
        phonenum = phonenum + '0'
        string = zero_removal(string)
    while string[25] > 0:
        phonenum = phonenum + '2'
        string = two_removal(string)
    while string[21] > 0:
        phonenum = phonenum + '4'
        string = four_removal(string)
    while string[27] > 0:
        phonenum = phonenum + '6'
        string = six_removal(string)
    while string[5] > 0:
        phonenum = phonenum + '8'
        string = eight_removal(string)
    while string[19] > 0 and string[7] > 0 and string[15] > 0 and string[1] > 1:
        phonenum = phonenum + '3'
        string = three_removal(string)
    while string[13] > 0 and string[11] > 0 and string[1] > 0:
        phonenum = phonenum + '1'
        string = one_removal(string)
    while string[23] > 0 and string[17] > 0:
        phonenum = phonenum + '7'
        string = seven_removal(string)
    while string[23] > 0 and string[3] > 0:
        phonenum = phonenum + '5'
        string = five_removal(string)
    while string[11] > 1 and string[9] > 0 and string[1] > 0:
        phonenum = phonenum + '9'
        string = nine_removal(string)
    aaa = ''.join(sorted(phonenum))
    return aaa


def cutevens(string):
    phonenum = ''
    while string[29] > 0:
        phonenum = phonenum + '0'
        string = zero_removal(string)
    while string[25] > 0:
        phonenum = phonenum + '2'
        string = two_removal(string)
    while string[21] > 0:
        phonenum = phonenum + '4'
        string = four_removal(string)
    while string[27] > 0:
        phonenum = phonenum + '6'
        string = six_removal(string)
    while string[5] > 0:
        phonenum = phonenum + '8'
        string = eight_removal(string)
    print string
    return phonenum
    
def zero_removal(array):
    arrear = array
    arrear[29] -= 1
    arrear[1] -= 1
    arrear[15] -= 1
    arrear[13] -= 1
    return arrear

def one_removal(array):
    arrear = array
    arrear[13] -= 1
    arrear[11] -= 1
    arrear[1] -= 1
    return arrear

def two_removal(array):
    arrear = array
    arrear[19] -= 1
    arrear[25] -= 1
    arrear[13] -= 1
    return arrear

def three_removal(array):
    arrear = array
    arrear[19] -= 1
    arrear[7] -= 1
    arrear[15] -= 1
    arrear[1] -= 2
    return arrear

def four_removal(array):
    arrear = array
    arrear[3] -= 1
    arrear[13] -= 1
    arrear[21] -= 1
    arrear[15] -= 1
    return arrear

def five_removal(array):
    arrear = array
    arrear[3] -= 1
    arrear[9] -= 1
    arrear[23] -= 1
    arrear[1] -= 1
    return arrear

def six_removal(array):
    arrear = array
    arrear[17] -= 1
    arrear[9] -= 1
    arrear[27] -= 1
    return arrear

def seven_removal(array):
    arrear = array
    arrear[17] -= 1
    arrear[1] -= 2
    arrear[23] -= 1
    arrear[11] -= 1
    return arrear

def eight_removal(array):
    arrear = array
    arrear[1] -= 1
    arrear[9] -= 1
    arrear[5] -= 1
    arrear[7] -= 1
    arrear[19] -= 1
    return arrear

def nine_removal(array):
    arrear = array
    arrear[11] -= 2
    arrear[9] -= 1
    arrear[1] -= 1
    return arrear

with open('A-large.in', 'rb') as text_file:
    t = text_file.readline().strip('\r\n')
    for line in text_file:
        line = line.strip('\r\n')
        print 'Case #%s: %s' % (case_num, numbermaker(counting_thingy(line)))
        case_num += 1


