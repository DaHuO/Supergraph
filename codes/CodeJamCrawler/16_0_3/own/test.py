def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)

def is_prime(n):
  if n == 2 or n == 3: return -1
  if n < 2 or n%2 == 0: return 2
  if n < 9: return -1
  if n%3 == 0: return 3
  r = int(n**0.5)
  f = 5
  while f <= 10000:
    #print '\t',f
    if n%f == 0: return f
    if n%(f+2) == 0: return f+2
    f +=6
  return -1

t = input()
s = raw_input()
arr = s.split(' ')
n = int(arr[0])
j = int(arr[1])


print "Case #1:"
counter =0
num = 0
while counter<j:

 
  num_str = str_base(num,2)
  x_str = '1'+num_str.zfill(n-2)+'1'
  arr = [-1]*9
  flag = True
  for base in range(2,10+1):
    tmp_num = int(x_str,base)
    divisor = is_prime(tmp_num)
    
    if divisor!= -1:
      arr[base-2] = divisor
    else:
      flag = False

  if flag:
    counter = counter +1
    str_arr = str(arr)
    str_arr=str_arr.replace(',','')
    str_arr=str_arr.replace('[','')
    str_arr=str_arr.replace(']','')
    print x_str,str_arr
  num = num+1

