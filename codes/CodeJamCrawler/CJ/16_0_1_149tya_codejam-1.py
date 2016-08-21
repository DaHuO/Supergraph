import unit4utils
import string

def fn(input):
    t=input[0]
    output=[]
    for i in input[1:]:
        m=i
        j=2
        temp=i
        result=[]
        repeat=[]
        while 1:
            while temp>0:
                rem=temp%10
                if rem not in result:
                    result.append(rem)
                temp/=10
            if i in repeat:
                output.append("INSOMNIA")
                break
            repeat.append(i)
            if len(result)!=10:
                i=m*j
                j+=1
                temp=i
                continue
            else:
                output.append(i)
                break
    return output


def read_words(filepointer):
    result=[]
    with open(filepointer,'r') as fd:
        for num in fd:
            num=int(num)
            result.append(num)
    return result

def write_words(filepointer,numbers):
    i=1
    with open(filepointer,'w') as fd:
        for num in numbers:
            num=str(num)
            if i==len(numbers):
                temp="Case #"+str(i)+": "+num
            else:
                temp="Case #"+str(i)+": "+num+"\n"
            fd.write(temp)
            i+=1

def main(source, destination):
    input=read_words(source)
    output=fn(input)
    write_words(destination,output)


def test_anagram_sort():
    source = unit4utils.get_input_file("A-large.in")
    destination = unit4utils.get_temp_file("largeoutput.out")
    main(source, destination)
