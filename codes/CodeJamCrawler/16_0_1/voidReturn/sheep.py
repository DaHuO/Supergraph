import sys

def main():

	filename = sys.argv[-1]

	r_file = open(filename, "r")
	w_file = open("output.txt", "w")

	T = int(r_file.readline())

	if T >= 1 and T <= 100:
		for cases in range(T):
			N = int(r_file.readline())

			if N >=0 and N <= 1000000:
				isSeen = [False, False, False, False, False, False, False, False, False, False]

				isSeen = updateArray(isSeen, str(N))

				index=2
				insomia = False
				while isSeen.count(True) is not 10:
					if index * N == (index-1) * N:
						print("Case #%s: Insomnia" %cases)
						w_file.write("Case #%s: Insomnia\n" %(cases+1))
						insomia = True
						break

					temp = index * N
					isSeen= updateArray(isSeen, str(temp))
					index+=1

				lastNum = (index-1)*N
				if not insomia:
					w_file.write(("Case #%s: %s\n" %((cases+1), lastNum)))
					print("Case #%s: %s" %(cases, lastNum))




def updateArray(arr, number):
	for digits in number:
		arr[int(digits)] = True
	return arr



main()