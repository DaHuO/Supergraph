def getNumbers(num):
    ret = []
    stringNum = str(num)
    for i in stringNum:
        if (int(i) not in ret):
            ret.append(int(i))
    return ret

def solve(req):
    index = 1
    numbers = []
    result = ''
    while (index < 1000):
        print str(index) + 'Try!!'
        print 'Input: ' + str(index*req)
        digitNumbers = getNumbers(req*index)
        for x in digitNumbers:
            if x not in numbers:
                numbers.append(x)
        if len(numbers) >= 10:
            print 'Result: ' + str(req*index)
            result = req*index
            break
        else:
            if index == 999:
                print 'Result: INSOMNIA'
                result = 'INSOMNIA'
                break
            index += 1
    return result

result = []
testCases = [0,1,2,11,1692,86364,652011,766971,531056,699299,386190,795778,907470,969177,999999,116547,12500,907214,855139,459789,219653,334159,159187,402979,335104,8,511003,94951,694327,520887,615892,766601,60701,999998,413929,125000,10,284982,465598,7,697945,692785,709677,999995,999991,125,725924,200,999992,718508,547018,717440,519515,1250,839136,124,165784,657748,61436,160515,6,49299,54700,25,166,363205,525772,337093,646257,40,418483,716928,1000000,344090,586334,899089,5,114551,315510,380354,381329,4,663394,31781,9,999997,436428,750836,999994,3,35143,109317,522460,999996,20,239365,999993,3940,527353,34]
for x in testCases:
    result.append(solve(x))
for i in range(len(result)):
    print 'Case #' + str(i+1) + ': ' + str(result[i])
