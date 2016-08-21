import sys

md = {}

def filldict():
    for i in xrange(10):
        md[i]=False

def verifTrue():
    _value = True
    for _, value in md.iteritems():
       _value = _value and value
       if not _value:
           return False

    return _value

def algo1(tt, numb):

    i = 0
    _value = 0

    while(True):
        i = i + 1
        _old_value = _value
        _value = i * int(numb)

        if _old_value == _value:
            return None

        for lett in str(_value):
            md[int(lett)]=True
            if verifTrue():
                return _value

def main():

    name="./small.txt"

    if len(sys.argv) > 1:
        name = sys.argv[1]

    fl = open(name, 'r')
    fl_wrt = open(name + "_reply", 'w')

    tt = int(fl.readline())
    i = 0

    reply = ''

    while (i < tt):
        i = i+1
       
        numb = fl.readline().rstrip()
        
        filldict()
        res1 = algo1(tt, numb)

        reply = reply + "Case #{0}: {1}\n".format(i, res1 or 'INSOMNIA')

    fl_wrt.write(reply)

if __name__ == "__main__":
    main()
