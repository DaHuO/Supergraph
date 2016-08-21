
input_file = open("B-large.in")
count = input_file.readline()
output_file = open("Revenge_of_the_Pancakes_result.txt", "w")
case = 0
for line in input_file:
    case += 1
    c = 0
    q = 0
    lst = []
    line = line.strip()
    lst += line
  #  print(lst)
    while q != len(lst):
        #print(q)
        q = 0
     #   print(lst)
        for i in lst:
            if i == "+":
                q += 1
        if q == len(lst):
            print(c, lst)
            output_file.write("Case #{!s}: ".format(case))
            output_file.write(str(c) + "\n")
            break
        c += 1
        if q != 0:
            for j in range(0 ,len(lst) - 1):
               # print(j)
                if lst[j] == "+" and lst[j + 1] == "-":
                    break

                if lst[j] == "-" and lst[j + 1] == "+":
                    break

            rp = lst[:j + 1]
          #  print(rp)
            for p in range(len(rp)):
               # print(p)
                if rp[p] == "+":
                    rp[p] = "-"
                else:
                    rp[p] = "+"

            rp.reverse()
          #  print(rp)

            lst = rp + lst[j + 1:]

        else:
            for p in range(len(lst)):
                if lst[p] == "-":
                    lst[p] = "+"
      #  output_file.write("Case #{!s}: ".format(case))
        #output_file.write(str(c) + "\n")
        print(c, lst)
        # else:
        #     print(c)
        #     break

