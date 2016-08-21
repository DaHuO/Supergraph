import sys
import string
import operator


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        inputs = f.read().splitlines()
    alphabet = list(string.ascii_uppercase)



    for case in range(int(inputs[0])):
        output_string = ''
        removal_list = []
        parties = {}
        temp_list = inputs[case * 2 + 2].split(' ')
        #print temp_list
        for party in range(len(temp_list)):
            parties[alphabet[party]] = int(temp_list[party])

        while sum(parties.values()) !=0:
            major = max(parties.iteritems(), key=operator.itemgetter(1))[0]
            #print major
            removal_list.append(major)
            parties[major] = parties[major] - 1
            if parties[max(parties.iteritems(), key=operator.itemgetter(1))[0]] > sum(parties.values()) - parties[max(parties.iteritems(), key=operator.itemgetter(1))[0]]:
                print "!!!!!!!!!!!!!!", parties[max(parties.iteritems(), key=operator.itemgetter(1))[0]], sum(parties.values()) - parties[max(parties.iteritems(), key=operator.itemgetter(1))[0]]
                res = str(removal_list[-1]) + str(max(parties.iteritems(), key=operator.itemgetter(1))[0])
                parties[max(parties.iteritems(), key=operator.itemgetter(1))[0]] = parties[max(parties.iteritems(), key=operator.itemgetter(1))[0]] - 1
            else:
                res = major
            output_string = output_string + ' ' +  res
            #for i in range(-2, -(len(output_string)), -4):
                #print i
                #temp_output_string = output_string[:i] + output_string[i+1:]

        #print removal_list
        with open('output.txt', 'a') as ouput_file:
                ouput_file.write("Case #" + str(case + 1) + ": " + output_string + '\n')


