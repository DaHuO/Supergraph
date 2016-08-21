test_cases=int(raw_input())
numbers=[]
for n in range(test_cases):
    numbers.append(raw_input())






for x in range(test_cases):
    number=numbers[x]
    all_seen=False
    loops=1
    original=int(number)

    seen0=False
    seen1=False
    seen2=False
    seen3=False
    seen4=False
    seen5=False
    seen6=False
    seen7=False
    seen8=False
    seen9=False


    while all_seen==False and number!="0":
        length=len(number)
        new=int(number)
        for n in range(length):
            if number[n]=="0" and seen0==False:
                seen0=True

            elif number[n]=="1" and seen1==False:
                seen1=True

            elif number[n]=="2" and seen2==False:
                seen2=True

            elif number[n]=="3" and seen3==False:
                seen3=True

            elif number[n]=="4" and seen4==False:
                seen4=True

            elif number[n]=="5" and seen5==False:
                seen5=True

            elif number[n]=="6" and seen6==False:
                seen6=True

            elif number[n]=="7" and seen7==False:
                seen7=True

            elif number[n]=="8" and seen8==False:
                seen8=True

            elif number[n] == "9" and seen9==False:
                seen9=True

        loops+=1
        if seen0==True and seen1==True and seen2==True and seen3==True and seen4==True and seen5==True and seen6==True and seen7==True and seen8==True and seen9==True:
            all_seen = True
        else:
            new=original*(loops)
            number=str(new)
    testcase=x+1
    testcase=str(testcase)
    if number!="0":
        print ("Case #")+testcase+(":"), number
    else:
        print ("Case #")+testcase+(":"), "INSOMNIA"










