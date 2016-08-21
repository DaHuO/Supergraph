input_file_name = "B-large"
output_file=open("{}.out" .format(input_file_name),'a')
import sys
sys.setrecursionlimit(10000)


def getFlips(cake, flips = 0):
    if '-' not in cake:
        return flips
    else:
        #Reverse cake present
        newCake = ""
        cakeSize = len(cake)
        if cake.startswith('+'):
            for idx, sign in enumerate(cake):
                if sign == '-':
                    top = idx
                    break
            for newSign in reversed(cake[:top]):
                newCake += '+' if newSign == '-' else '-'
            newCake = newCake + cake[top:]
            flips = flips + 1
            return getFlips(newCake, flips)
        else:
            reverseCake = reversed(cake)
            for idx, sign in enumerate(reverseCake):
                if sign == '-':
                    bottom = cakeSize - idx
                    break

            for newSign in reversed(cake[:bottom]):
                newCake += '+' if newSign == '-' else '-'

            if newCake == cake[:bottom]:
                print "New cake same"

            flips = flips + 1
            return getFlips(newCake, flips)

with open("{}.in".format(input_file_name)) as input_file:
    counter=0
    try:
        totalInput=long(input_file.readline())
        for i in range(totalInput):
            try:
                value = getFlips(str(input_file.readline()).rstrip('\r\n'))
            except Exception as e:
                print e , str(input_file.readline()).rstrip('\r\n')
            if i == totalInput-1:
                output_file.write("Case #{}: ".format(i+1)+str(value))
            else:
                output_file.write("Case #{}: ".format(i+1)+str(value)+"\n")
    except Exception as e:
        pass


print "done"
output_file.close()