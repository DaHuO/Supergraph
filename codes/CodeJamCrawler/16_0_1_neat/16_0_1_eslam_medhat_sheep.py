def main():
    #read in file
    File_tiny="tiny.in"
    File_small = "A-small-attempt0.in"
    File_large = "A-large.in"
    in_f = open(File_large , "r")
    t_cases = int( str.lstrip(in_f.next()) )

    #init out file
    out_f= open( "rotate_out.txt", "w" )

    


    #main loop
    for case in range(t_cases):
        num = int(str.lstrip(in_f.next()))
        decs = [str(i) for i in range(10)]
        counter=0
        if (num == 0):
            out_f.write("Case #"+str(case+1)+": " + "INSOMNIA"+"\n")
        else:
            while(max(decs)>0):
                #print "================="
                #print decs
                #print counter
                #print str(num*(counter+1))
                #print "================="
                for i in decs:
                    if((str(num*(counter+1)).find(str(i)))>=0):
                        decs[int(i)]=-1
                counter = counter + 1
            out_f.write("Case #"+str(case+1)+": " + str(num*(counter))+"\n")
            
    #close files
    in_f.close()
    out_f.close()
    return



main()
