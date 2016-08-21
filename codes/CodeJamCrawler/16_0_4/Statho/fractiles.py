
import math

txt = open("D-small-attempt0.in", "r")

out = open("output4.txt", "w")
dic = {}
case = 0
yolo = 0

for k in range(int(txt.readline().strip())):
	for i in txt:
		case = case + 1
		metr = 0
		i = i.split(' ')
		count = int(i[1]) - 1
		out.write("Case #"+  str(case) + ":")
		if int(i[1]) == 1 or int(i[0]) == int(i[2]):
			if int(i[0]) > int(i[2]):
				out.write(" IMPOSSIBLE\n")
			else:
				for j in range(int(i[0])) :
					out.write(" " + str(j + 1))
				out.write('\n')
		elif math.log(int(i[0]), int(i[1])) > int(i[2]):
			out.write(" IMPOSSIBLE\n")
		else:
			j = 0 
			while j < int(i[0]):
				while count > 0 and j < int(i[0]):
					metr = metr + pow(int(i[0]),count) * j
					count = count - 1
					j = j + 1
				out.write(' ' + str(metr + 1))
				metr = 0
				count = int(i[1]) - 1
				j = j + 1
				yolo = yolo + 1
				out.write("IMPOSSIBLE!!!\n")
			if yolo >= int(i[2]):
				yolo = 0
				out.write('\n')
			
			
			