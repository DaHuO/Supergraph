import random
import math

input_file = open("Coin_Jam.txt")
count = input_file.readline()
output_file = open("Coin_Jam_result2.txt", "w")
case = 0
n, j = (int(i) for i in input_file.readline().split())
print(n, j)
pool = ('0', '1')
numbers = []

output_file.write("Case #{!s}: ".format(1))
output_file.write("\n")

def gen(n):
    number = "1"
    for i in range(n - 2):
        number += random.choice(pool)
    number += '1'
    number = int(number)
   # print(number)
    return number

while len(numbers) != 2 **(n-2):
    m = gen(n)
    if m not in numbers:
        numbers.append(m)
print(numbers)

result = {}
counter = 0
for num in numbers:
    if counter == j:
        break
    #num = 100011

    if num == 100011:
        print("hi")
    result[num] = []
    div = ""
    div1 = []
    for i in range(2, 11):
     #   f = str(round(num**0.5))
        for q in range(2, int(math.sqrt(int(str(num), i)))):
            if int(str(num), i) % q == 0 :
                div += str(q) + " "
                div1.append(q)

              #  print(div)
                break
    if len(div1) <= 8:
       # print(div)
        #div = []
        print("fail")
           # break
    else:
       # print(div)
        counter += 1
        output_file.write(str(num) + " " + div + "\n")
        result[num].append(div)





#
# for j in result:
#     if len(result[j]) != 0:
#         for letter in result[j]:
#             output_file.write(str(letter) + " ")
#         output_file.write("\n")

print(counter)
#print(result[100011])








