class BaseConverter(object):
    decimal_digits = "0123456789"
    
    def __init__(self, digits=None):
        if digits is None:
            pass
        else:
            self.digits = digits
    
    def from_decimal(self, i):
        return self.convert(i, self.decimal_digits, self.digits)
    
    def to_decimal(self, s):
        return int(self.convert(s, self.digits, self.decimal_digits))
    
    def convert(number, fromdigits, todigits):
        # Based on http://code.activestate.com/recipes/111286/
        if str(number)[0] == '-':
            number = str(number)[1:]
            neg = 1
        else:
            neg = 0

        # make an integer out of the number
        x = 0
        for digit in str(number):
            x = x * len(fromdigits) + fromdigits.index(digit)
        if x == 0:
            res = todigits[0]
        else:
            res = ""
            while x > 0:
                digit = x % len(todigits)
                res = todigits[digit] + res
                x = int(x / len(todigits))
            if neg:
                res = '-' + res
        return res
    convert = staticmethod(convert)
l=[]
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: 
      l.append(2)
      return False    #add 2 into the list
  if n < 9: return True
  if n%3 == 0: 
      l.append(3)
      return False      #add 3 into the list
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: 
        l.append(f)
        return False    #add f into the list
    if n%(f+2) == 0: 
        l.append(f+2)
        return False  #add f+2 into the list
    f +=6
  return True
bc=BaseConverter()
def check(n):
    if is_prime(int(bc.convert(n,'01', '0123456789'))):
        return False
    if is_prime(int(bc.convert(n,'012', '0123456789'))):
        return False
    if is_prime(int(bc.convert(n,'0123', '0123456789'))):
        return False
    if is_prime(int(bc.convert(n,'01234', '0123456789'))):
        return False
    if is_prime(int(bc.convert(n,'012345', '0123456789'))):
        return False
    if is_prime(int(bc.convert(n,'0123456', '0123456789'))):
        return False
    if is_prime(int(bc.convert(n,'01234567', '0123456789'))):
        return False
    if is_prime(int(bc.convert(n,'012345678', '0123456789'))):
        return False
    if is_prime(n):
        return False
    return True
t=int(raw_input())
for k in range(t):
    li=map(int,raw_input().split())
    n,j=li[0],li[1]
    low=(2**(n-1))+1
    high=0
    for i in range(n):
        high=high+(2**i)
    print "Case #"+`k+1`+":"
    binary=BaseConverter('01')
    for i in range(low,high+1):
        l=[]
        if check(int(binary.from_decimal(i)))==True:
            o=binary.from_decimal(i)
            if o[len(o)-1]=='1':
                print o,l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8]
                j=j-1
        if j==0:
            break
        
    



