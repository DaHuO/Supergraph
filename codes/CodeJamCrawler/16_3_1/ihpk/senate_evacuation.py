import string

def senate_evacuation(file_name):
    read_file_name = file_name
    write_file_name = file_name + ' - answer.txt'
    
    read_file = open(read_file_name)
    write_file = open(write_file_name, "w")
    
    cases = int(read_file.readline())
    
    current_case = 1
    
    while current_case <= cases:
        parties = int(read_file.readline())
        senator_distribution = read_file.readline()
        output = build_evacuation_plan(parties, senator_distribution)
        file_output = "Case #{0}: {1}\n".format(current_case, output)
        print(file_output)
        write_file.write(file_output)
        current_case += 1

def build_evacuation_plan(parties, senator_distribution):
    senator_split = senator_distribution.split()
    party_names = list(string.ascii_uppercase)
    pop_to_party = {}
    
    total_number_of_senators = 0
    highest_population_in_party = 0
    
    i = 0
    while i < parties:
        party = party_names[i]
        number_of_senators = int(senator_split[i])
        
        
        highest_population_in_party = max(highest_population_in_party, number_of_senators - 1)
        total_number_of_senators += number_of_senators

        j = 0
        while j < number_of_senators:
            if j in pop_to_party:
                pop_to_party[j].append(party)
            else:
                pop_to_party[j] = [party]
            j += 1
        i += 1
    print(pop_to_party)
    
    exit_plan = ""
    
    while total_number_of_senators > 0:
        if total_number_of_senators == 3: #grab 1 senator
            highest_population_in_party, senator_1 = grab_next_senator(pop_to_party, highest_population_in_party)
            total_number_of_senators -= 2
            exit_plan += senator_1 + " "
        else: #grab 2 senators
            highest_population_in_party, senator_1 = grab_next_senator(pop_to_party, highest_population_in_party)
            highest_population_in_party, senator_2 = grab_next_senator(pop_to_party, highest_population_in_party)
            total_number_of_senators -= 2
            exit_plan += senator_1 + senator_2 + " "
    
    return(exit_plan)
    
def grab_next_senator(pop_to_party, highest_population_in_party):
    senators_at_pop = pop_to_party[highest_population_in_party]
    if len(senators_at_pop) > 0:
        return highest_population_in_party, senators_at_pop.pop()
    else:
        highest_population_in_party -= 1
        senators_at_pop = pop_to_party[highest_population_in_party]        
        return highest_population_in_party, senators_at_pop.pop()
    

"""
def build_evacuation_plan(parties, senator_distribution):
    senator_split = senator_distribution.split()
    party_names = list(string.ascii_uppercase)
    party_to_pop = {}
    pop_to_party = {}
    total_number_of_senators = 0
    highest_population_in_party = 0
    i = 0
    while i < parties:
        party = party_names[i]
        number_of_senators = int(senator_split[i])
        party_to_pop[party] = number_of_senators
        pop_to_party[number_of_senators] = party
        total_number_of_senators += number_of_senators
        i += 1
    
    exit_plan = ""
    while highest_population_in_party > 0:
        if total_number_of_senators == 3: #grab 1 senator
            pass
        else: #grab 2 senators
    """
            
        
    
    

if __name__ == "__main__":
    senate_evacuation("test.txt")
    #senate_evacuation("A-small-attempt0.in")
    senate_evacuation("A-large.in")