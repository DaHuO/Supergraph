NEGATIVE = '-'
POSITIVE = '+'

def pancakes_fliper(pancakes_order):
    count=0
    while NEGATIVE in pancakes_order:
        first_sequence = first_seq(pancakes_order) 
        pancakes_order = flip(pancakes_order[:first_sequence]) + pancakes_order[first_sequence:]
        count += 1
    return count

    
def first_seq(pancakes_order):
    first_kind = pancakes_order[0]
    count = 0
    while pancakes_order and first_kind == pancakes_order[0]:
        count += 1
        pancakes_order = pancakes_order[1:]
    return count        

def flip(pancakes_order):
    length = len(pancakes_order)
    for i in range(int(length/2)):
        temp = pancakes_order[i]
        pancakes_order[i] = change_status(pancakes_order[length-i-1])
        pancakes_order[length-i-1] = change_status(temp)
    if length%2 == 1:
        pancakes_order[int(length/2)] = change_status(pancakes_order[int(length/2)])
    return pancakes_order
#CRed
def change_status(pancake_status):
    if pancake_status == '+':
        return '-'
    return '+'

def last_index_of(order, char):
    return len(order) - order[::-1].index(char)

def main():
    T=int(input('Enter number of test cases:'))
    dest_fd=open(r'C:\Users\Alon_3\Desktop\Code_jam\output_b_pancakes.txt', 'w')
    for case in range(T):
        order = (input())
        dest_fd.write('Case #'+str(case+1)+': '+ str(pancakes_fliper(list(order)))+'\r\n')
    dest_fd.close()

if __name__ == '__main__':
    main()