a = input()
b=[]
for i in range(a):
    b.append([input(),[]])
    b[i][1] = map(int,raw_input().split(" "))



def evac(lst):
    num = lst[0]
    series  = lst[1]
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    srt =[]
    for i in range(num):
        srt.append([series[i],alpha[i]])
    srt = sorted(srt)
    output = ""
    if srt[-1][0] > srt[-2][0]:
        output += (srt[-1][1] + " ") * (srt[-1][0] - srt[-2][0])
        srt[-1][0] = srt[-2][0]

    if len(srt)-2:
        for i in range(len(srt) - 2):
            output += (srt[i][1] + " ") * (srt[i][0])
    for i in range(srt[-1][0]):
        output += srt[-1][1] + srt[-2][1] + " "

    result =""
    for i in range(len(output)):
        result += output[i]
    return result

for i in range(a):
    print "Case #" + str(i+1) + ":",evac(b[i])
