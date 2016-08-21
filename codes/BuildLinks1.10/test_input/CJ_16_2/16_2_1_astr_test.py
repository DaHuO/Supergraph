import collections
import math
# debug=False
# with open('A-small-practice.in') as f:
# debug=True
with open('A-large.in') as f:
    content = f.readlines()

def removeDigit(item,charCounter,phoneNumber,x):
    for x in range(charCounter[x]):
        phoneNumber.append(charNumberMap[item])
        for x in item:
            charCounter[x]-=1
charNumberMap={}
def getPhoneNumber(S):
    global charNumberMap
    charCounter={}
    phoneNumber=[]
    charNumberMap={'ZERO':'0','ONE':'1','TWO':'2','THREE':'3','FOUR':'4','FIVE':'5','SIX':'6','SEVEN':'7','EIGHT':'8','NINE':'9'}
    for x in S:
        if x in charCounter:
            charCounter[x]+=1
        else:
            charCounter[x]=1
    # print(charCounter)
    if "Z" in charCounter and charCounter['Z']>0:
        removeDigit("ZERO",charCounter,phoneNumber,'Z')
    if 'W' in charCounter and charCounter['W']>0:
        removeDigit("TWO",charCounter,phoneNumber,'W')
    # print(charCounter)
    if 'X' in charCounter and charCounter['X']>0:
        removeDigit("SIX",charCounter,phoneNumber,'X')
    if 'G' in charCounter and charCounter['G']>0:
        removeDigit("EIGHT",charCounter,phoneNumber,'G')
    # print(charCounter)
    if 'U' in charCounter and charCounter['U']>0:
        removeDigit("FOUR",charCounter,phoneNumber,'U')
    if 'F' in charCounter and charCounter['F']>0:
        removeDigit("FIVE",charCounter,phoneNumber,'F')
    # print(charCounter)
    if 'S' in charCounter and charCounter['S']>0:
        removeDigit("SEVEN",charCounter,phoneNumber,'S')
    if 'T' in charCounter and charCounter['T']>0:
        removeDigit("THREE",charCounter,phoneNumber,'T')
    # print(charCounter)
    if 'I' in charCounter and charCounter['I']>0:
        removeDigit("NINE",charCounter,phoneNumber,'I')
    if 'O' in charCounter and charCounter['O']>0:
        removeDigit("ONE",charCounter,phoneNumber,'O')
    # print(charCounter)
    phoneNumber.sort()
    return ''.join(phoneNumber)



for tc in range(int(content.pop(0))):
    S = content.pop(0).strip()       
    print("Case #%d: %s" % (tc + 1, getPhoneNumber(S)))
