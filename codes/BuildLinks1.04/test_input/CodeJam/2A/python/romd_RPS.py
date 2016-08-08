LINES_FOR_EACH_INPUT = 1
INPUT_FILE_NAME = 'A-large.in'
OUTPUT_FILE_NAME = 'A-large.out'

def do_case(parsed):
        
        return bestComp(parsed[1],parsed[2],parsed[3],0)
def expand_orderd(round_num,letter):
        rep={
                "0p":"PRRS",
                "0s":"PRPS",
                "0r":"PSRS",
                "1p":"SRPR",
                "1s":"SPPR",
                "1r":"SPSR",
                "2p":"RSRP",
                "2s":"RPSP",
                "2r":"RSSP"}
        return rep[str(round_num%3)+str(letter)]
def bestComp(R,P,S,round_num):
        players=R+P+S
        if(players==1):
                if R==1:
                        return "R"
                if P==1:
                        return "P"
                if S==1:
                        return "S"
        
        if players==2:
                if R==2 or S==2 or P==2:
                        return "IMPOSSIBLE"
                rep2={
                "0011":"PS",
                "0101":"RS",
                "0110":"PR",
                "1011":"SP",
                "1101":"SR",
                "1110":"PR",
                "2011":"SP",
                "2101":"RS",
                "2110":"RP"}
                return rep2[str(round_num%3)+str(R)+str(P)+str(S)]
        if R<players/4 or S<players/4 or P<players/4:
                return "IMPOSSIBLE"
        temp=bestComp(int(S-players/4),int(R-players/4),int(P-players/4),round_num+1)
        if temp=="IMPOSSIBLE":
                return temp
        temp=temp.replace("R","r")
        temp=temp.replace("P","p")
        temp=temp.replace("S","s")
        temp=temp.replace("r",expand_orderd(round_num,"r"))
        temp=temp.replace("p",expand_orderd(round_num,"p"))
        temp=temp.replace("s",expand_orderd(round_num,"s"))
        return temp
        
def do_parse(input):
        return [int(num) for num in input[0].rstrip().split(" ")]     

def main():
        input_f = open(INPUT_FILE_NAME, 'r')
        output = []
	
        num_of_test_cases = int(input_f.readline(), 10)
	
        input_lines = input_f.readlines()
	
        for test_case in range(num_of_test_cases):
                parsed_input = do_parse(input_lines[test_case*LINES_FOR_EACH_INPUT : (test_case + 1) * LINES_FOR_EACH_INPUT])
                output.append('Case #' + str(test_case + 1) + ': ' + do_case(parsed_input))

        output_f = open(OUTPUT_FILE_NAME, 'w')
        output_f.write('\n'.join(output))
	
        input_f.close()
        output_f.close()
	
if __name__ == '__main__':
        main()
